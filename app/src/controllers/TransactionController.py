from typing import Union, Optional

from fastapi import APIRouter, Depends
from fastapi_pagination import Page
from app.src.schemas.requests.TransactionApiSchema import TransactionApiSchema
from app.src.schemas.requests.TransactionPageSchema import TransactionPage, DealPage, DealPageFilter, \
    TransactionPageFilter
from app.src.schemas.requests.enums.types import TransactionOrDeal
from app.src.schemas.response.models import TransactionCreationResponse
from app.src.services.TransactionInjectionType import TransactionInjection, TransactionFiltersInjection
from app.src.services.TransactionApiService import TransactionApiService
from fastapi_pagination import Params

from app.src.services.response.handlers import AuthorizationHandler

router = APIRouter(tags=["Transactions"], prefix="/transaction")


@router.post("/filters", response_model=TransactionPageFilter | DealPageFilter)
async def get_transaction_filters(transaction_type: TransactionOrDeal,
                                 user: str = Depends(AuthorizationHandler)):
    service: TransactionApiService = TransactionApiService(transaction=transaction_type, user=user)
    return service.get_filter_details()


@router.post("/details", response_model=list[TransactionApiSchema])
async def get_transaction_detail(transaction_type: TransactionOrDeal,
                                 ids: list[int],
                                 user: str = Depends(AuthorizationHandler)):
    service: TransactionApiService = TransactionApiService(transaction=transaction_type)
    return service.get_structured_transaction(ids)


@router.post("/transactions", response_model=Page[TransactionPage])
async def get_transactions(filters: Optional[TransactionPageFilter] = None,
                           paginator: Params = Depends(),
                           user: str = Depends(AuthorizationHandler)):
    service: TransactionApiService = TransactionApiService(transaction=TransactionOrDeal.TRANSACTION, data=filters,
                                                    paginator=paginator, user=user)
    if filters := filters:
        service.save(TransactionFiltersInjection)
        for field, value in filters:
            service.filter_by(field, value)
    response = service.query_execute()
    return response


@router.post("/deals", response_model=Page[DealPage])
async def get_deals(filters: Optional[DealPageFilter] = None, paginator: Params = Depends(),
                    user: str = Depends(AuthorizationHandler)):
    service: TransactionApiService = TransactionApiService(transaction=TransactionOrDeal.DEAL,data=filters,
                                                    paginator=paginator,user=user)
    if filters := filters:
        service.save(TransactionFiltersInjection)
        for field, value in filters:
            service.filter_by(field, value)
    response = service.query_execute()
    return response


@router.post("/create_resource", response_model=TransactionCreationResponse)
async def save_transactions(data: TransactionApiSchema):
    transaction = TransactionOrDeal.TRANSACTION if data.recId else TransactionOrDeal.DEAL
    service: TransactionApiService = TransactionApiService(transaction=transaction, data=data)
    return service.save(TransactionInjection)
