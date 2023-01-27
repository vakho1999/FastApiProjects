from typing import Union
from uuid import UUID

from fastapi import APIRouter, Depends


from app.src.schemas.requests.TransactionSettings import TransactionSettings, DealSettings
from app.src.schemas.requests.enums.types import TransactionOrDeal
from app.src.schemas.response.models import TransactionCreationResponse
from app.src.services.DataTableService import DataTableService
from app.src.services.TransactionInjectionType import DataTableInjection
from app.src.services.response.handlers import AuthorizationHandler

router = APIRouter(tags=["DataTable Settings"], prefix="/datatable")


@router.get("/get_settings", response_model=Union[DealSettings, TransactionSettings])
async def get_settings(transaction_type: TransactionOrDeal, user: UUID = Depends(AuthorizationHandler)):
    dataTableService = DataTableService(transaction=transaction_type, user=user)

    return dataTableService.get_filter_details("data")[0]


@router.post("/save_settings", response_model=TransactionCreationResponse)
async def save_settings(transaction_type: TransactionOrDeal, data: Union[DealSettings, TransactionSettings],
                        user: UUID = Depends(AuthorizationHandler)):
    dataTableService = DataTableService(transaction=transaction_type, data=data, user=user)
    return dataTableService.save(DataTableInjection)
