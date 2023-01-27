from enum import Enum
from typing import Union

from pydantic import BaseModel
from pydantic.class_validators import List



class BaseEnum(str, Enum):
    Id = "Id"
    Purpose = "Purpose"
    Scenario = "Scenario"
    Currency = "Currency"
    Amount = "Amount"
    AmountToGel = "AmountToGel"


class DealSettingsEnum(str, Enum):
    DealType = "DealType"
    DealForm = "DealForm"
    Participate = "Participate"


class TransactionSettingsEnum(str, Enum):
    TransactionType = "TransactionType"
    DebitorBank = "DebitorBank"
    CreditorBank = "CreditorBank"
    DebitorAccount = "DebitorAccount"
    CreditorAccount = "CreditorAccount"
    Creditor = "Creditor"
    Debitor = "Debitor"


class DealProperty(BaseModel):
    width: int
    name: Union[DealSettingsEnum, BaseEnum]


class TransactionProperty(BaseModel):
    width: int
    name: Union[TransactionSettingsEnum, BaseEnum]


class DealSettings(BaseModel):
    data: List[DealProperty]


class TransactionSettings(BaseModel):
    data: List[TransactionProperty]
