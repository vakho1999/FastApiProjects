from enum import Enum

from app.src.schemas.requests.enums.constants.transactionConstant import TransactionTypesList, NbgTransactionTypesList, \
    LegalFormTypesList, AccountTypesList, ActivityAreaTypesList



class TransactionOrDeal(Enum):
    TRANSACTION = "TR"
    DEAL = "DL"


class CurrencyType(Enum):
    GEL = "GEL"
    USD = "USD"
    EUR = "EUR"


class DocumentType(Enum):
    GeorgianPassport = "GeorgianPassport"
    ForeignPassport = "ForeignPassport"
    ResidenceCard = "ResidenceCard"
    Other = "Other"
    UNKNOWN = "UNKNOWN"


class TransactionSubType(Enum):
    SWIFT = "SWIFT"
    ANELIK = "Anelik"
    KORONA = "Korona"

class RiskLevelType(Enum):
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    RED = "RED"

class RelatedType(Enum):
    FOUNDER = "FOUNDER"
    DIRECTOR = "DIRECTOR"
    BENEFICIARY = "BENEFICIARY"
    SHAREHOLDER = "SHAREHOLDER"
    TRUSTEE = "TRUSTEE"

TransactionType: Enum = Enum('TransactionType', dict(zip(TransactionTypesList, TransactionTypesList)))
NbgTransactionType: Enum = Enum('NbgTransactionType', dict(zip(NbgTransactionTypesList, NbgTransactionTypesList)))
LegalFormType: Enum = Enum('LegalFormType', dict(zip(LegalFormTypesList, LegalFormTypesList)))
AccountType: Enum = Enum('AccountType', dict(zip(AccountTypesList, AccountTypesList)))
ActivityAreaType: Enum = Enum('ActivityAreaType', dict(zip(ActivityAreaTypesList, ActivityAreaTypesList)))
