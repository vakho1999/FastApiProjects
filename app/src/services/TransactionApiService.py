import datetime
import json
from typing import Any, Union, Optional
from uuid import UUID

from fastapi_pagination.bases import AbstractPage
from sqlalchemy import not_
from sqlalchemy.orm import Query, session
from app.src.db.utils import get_db
from app.src.designes.Factory import TransactionModelFactory
from app.src.models.Transaction import Transaction, Deal, StructuredTransaction, TransactionFilters, DealFilters
from app.src.schemas.requests import TransactionApiSchema
from app.src.schemas.requests.enums.types import TransactionOrDeal
from app.src.schemas.response.enums.types import HttpStatusCodes
from app.src.services.interfaces.TransactionInterface import TrasactionDataInjectionServiceImpl, \
    TransactionApiServiceImpl
from fastapi_pagination import paginate
from app.src.services.response.handlers import ResponseHandler
from app.src.services.utils.util import filter_transaction


class TransactionApiService(TransactionApiServiceImpl):

    @ResponseHandler(code=HttpStatusCodes.OK)
    def get_filter_details(self, filters: str = "filter") -> dict[str, Any]:
        instance = self._get_instance(filters)
        if data := self.session.query(instance.data).filter_by(uid=self.user).first() or []:
            return data

    def __init__(self, user=None, data=None, transaction=None, paginator=None):
        self.data: Optional[TransactionApiSchema] | TransactionFilters | DealFilters = data
        self.user = user
        self.instances: Union[tuple[Transaction, TransactionFilters],
                              tuple[Deal, DealFilters]] = TransactionModelFactory(transaction)
        self.session: session = next(get_db())
        self.query: Query = self.session.query(self._get_instance("data"))
        self.params: Optional[dict[str, Union[str, int]]] = paginator

    @ResponseHandler(code=HttpStatusCodes.OK)
    def get_structured_transaction(self, ids: list[id]) -> list[dict[Any, Any]]:
        instance = self._get_instance("data")
        self.query = self.query.join(StructuredTransaction).with_entities(StructuredTransaction.data). \
            filter(instance.id.in_(ids)).all()
        return [json.loads(val[0]) for val in self.query]

    @ResponseHandler(code=HttpStatusCodes.OK)
    def filter_by(self, field: str, value: dict[str,Union[str, int]]) -> None:
        if value["value"]:
            filter_transaction(self, field, value)

    @ResponseHandler(code=HttpStatusCodes.OK)
    def query_execute(self) -> AbstractPage[Union[Transaction, Deal]]:
        instance = self._get_instance("filter")
        if instance := self.user and self.session.query(instance.data).filter_by(uid=self.user).first():
            for field, value in instance.data.items():
                self.filter_by(field, value)

        return paginate(self.query.all(), self.params)

    def _get_instance(self, type: str):
        factory = {
            "filter": 1,
            "data": 0
        }
        return self.instances[factory[type]]

    @ResponseHandler(code=HttpStatusCodes.CREATED)
    def save(self, service: TrasactionDataInjectionServiceImpl) -> None:
        service.save(self.instances, self.data, self.session, self.user)
        # transaction: StructuredTransaction = StructuredTransaction(data=self.data.to_json())
        # instance = self.instance(self.data)
        # instance.detail = transaction
        #
        # self.session.add(instance)
        # self.session.commit()
