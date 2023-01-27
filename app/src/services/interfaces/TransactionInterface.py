from uuid import UUID
from abc import ABC, abstractmethod
from typing import Any, Union, Optional

from fastapi_pagination import Params
from fastapi_pagination.bases import AbstractPage
from sqlalchemy.orm import Query, Session

from app.src.models.Transaction import Transaction, Deal, TransactionFilters, DealFilters


class TrasactionDataInjectionServiceImpl(ABC):

    @classmethod
    @abstractmethod
    def save(cls, instance: Union[tuple[Transaction, TransactionFilters],
                             tuple[Deal, DealFilters]], data: Any, session: Session, user: Optional[UUID] = None) -> ...:
        """this method saves object into database"""
        ...


class StandardApiServiceImpl(ABC):


    @abstractmethod
    def filter_by(self, field: Any, value: Any) -> Query:
        """filter and retrieves transactions by parameter, Pagination should be by default """
        ...

    @abstractmethod
    def query_execute(self) -> AbstractPage[Any]:
        """execute query"""
        ...
    @abstractmethod
    def _get_instance(self, type: str) -> dict: ...


    @abstractmethod
    def get_structured_transaction(self, ids: list[id]) -> None:
        """get transaction detail"""
        ...
    @abstractmethod
    def save(self, service: TrasactionDataInjectionServiceImpl) -> None:
        """save transaction data"""
        ...






class TransactionApiServiceImpl(StandardApiServiceImpl):




    @abstractmethod
    def get_filter_details(self) -> dict[str, Any]:
        """get transaction detail"""
        ...



