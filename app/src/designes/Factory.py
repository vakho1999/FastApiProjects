from dataclasses import dataclass, field
from typing import Union, Dict, Type, Tuple

from app.src.models.Transaction import Transaction, Deal, TransactionFilters, DealFilters, TransactionTableSettings, \
    DealTableSettings
from app.src.schemas.requests.enums.types import TransactionOrDeal


@dataclass
class TransactionModelFactory:
    __factory: Dict[TransactionOrDeal, Type[Union[Transaction, Deal]]] | None = field(default_factory=lambda: {
        TransactionOrDeal.TRANSACTION: (Transaction, TransactionFilters),
        TransactionOrDeal.DEAL: (Deal, DealFilters),
    })

    def __call__(self, type: TransactionOrDeal)-> Type[Union[Transaction, Deal]]:
        return self.__factory[type]


@dataclass
class DataTableFactory:
    __factory: Dict[TransactionOrDeal, Type[Union[TransactionTableSettings, DealTableSettings]]] | None = field(default_factory=lambda: {
        TransactionOrDeal.TRANSACTION: TransactionTableSettings,
        TransactionOrDeal.DEAL: DealTableSettings,

    })

    def __call__(self, type: TransactionOrDeal) -> tuple[Type[TransactionTableSettings | DealTableSettings], None]:
        return self.__factory[type], None


DataTableFactory = DataTableFactory()
TransactionModelFactory = TransactionModelFactory()
