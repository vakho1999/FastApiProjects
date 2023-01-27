from typing import Union, Optional, Any

from fastapi_pagination.bases import AbstractPage
from sqlalchemy.orm import Query, session

from app.src.db.utils import get_db
from app.src.designes.Factory import DataTableFactory
from app.src.models.Transaction import TransactionTableSettings, DealTableSettings
from app.src.schemas.requests.TransactionSettings import TransactionSettings, DealSettings
from app.src.services.TransactionApiService import TransactionApiService


class DataTableService(TransactionApiService):

    def __init__(self, user=None, data=None, transaction=None, paginator=None):
        super().__init__(user, None, transaction, paginator)
        self.user = user
        self.session: session = next(get_db())
        self.data: TransactionSettings | DealSettings = data
        self.instances: Union[tuple[TransactionTableSettings, None],
                              tuple[DealTableSettings, None]] = DataTableFactory(transaction)
        self.query: Query = self.session.query(self._get_instance("data"))

    def query_execute(self) -> ...:
        raise NotImplementedError("not implemented method query_execute")

    def filter_by(self, field: str, value: Union[str, int]) -> None:
        raise NotImplementedError("not implemented method filter_by")

    def get_structured_transaction(self, filters: str) -> None:
        raise NotImplementedError("not implemented method get_structured_transaction")

