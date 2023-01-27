from enum import Enum
import json

from pydantic import BaseModel
from pydantic.class_validators import List, Optional
from pydantic.validators import date, datetime
from app.src.schemas.requests.enums.types import TransactionSubType, DocumentType, \
    LegalFormType, TransactionType, NbgTransactionType, AccountType, RiskLevelType, RelatedType
from app.src.schemas.requests.types.types import Number


class CountryRequest(BaseModel):
    iso2: str
    iso3: str


class CustomerAltName(BaseModel):
    id: int
    createTime: datetime
    updateTime: datetime
    name: str


class RelatedPeople(BaseModel):
    relatedId: str
    fullName: str
    address: str
    resident: CountryRequest
    citizenship: CountryRequest
    passportId: str
    documentId: str
    georgianIdNumber: str
    legalAddress: str
    actualAddress: str
    passportIssuerAddress: str
    identificationIssuerAddress: str
    taxPayerRegCountry: str
    bic: str
    birthDate: date
    keywords: List[str]
    percentShare: Number
    juridical: bool
    relatedType: RelatedType
    pep: bool


class TransactionParticipant(BaseModel):
    resident: CountryRequest
    balance: Number
    clientId: str
    altNames: List[CustomerAltName]
    note: str
    clientNo: int
    juridical: bool
    citizenship: CountryRequest
    bankRegDate: date
    mail: str
    phone: str
    georgianIdNumber: str
    passportId: str
    address: str
    gender: str
    birthDate: date
    birthCountry: str
    birthPlace: str
    documentType: DocumentType
    issuerName: str
    firstName: str
    lastName: str
    serie: str
    number: str
    after: date
    before: date
    documentIdentifier: str
    issuingCountry: str
    jobTitle: str
    fullName: str
    legalForm: LegalFormType
    regNumber: str
    regDate: date
    regOrganization: str
    regCountry: str
    legalAddress: str
    actualAddress: str
    taxPayerId: str
    accountNumber: str
    accountType: AccountType
    bankName: str
    bic: str
    bankCountry: str
    bankPlace: str
    accountOpeningDate: date
    accountClosingDate: date
    riskLevel: RiskLevelType
    pep: bool
    swift50: str
    ITRS: str
    taxPayerRegCountry: str
    relatedPeople: List[RelatedPeople]


class TransactionApiSchema(BaseModel):
    amount: Optional[Number]
    iso: Optional[str]
    purpose: Optional[str]
    location: Optional[str]
    dealId: Optional[str] = None
    recId: Optional[str] = None
    bankIdentifier: Optional[str]
    docDate: Optional[date]
    transactionType: Optional[TransactionType]
    amountEqu: Optional[Number]
    dealform: Optional[str] = ""
    credit: Optional[TransactionParticipant]
    debit: Optional[TransactionParticipant]
    participate: Optional[TransactionParticipant]
    cashPayment: Optional[bool]
    extraPurpose: Optional[str]
    nbgTransactionType: Optional[NbgTransactionType]
    transactionSubType: Optional[TransactionSubType]
    dealdesc: Optional[str]
    distance: Optional[bool]
    intBank: Optional[dict[str, str]]

    @staticmethod
    def default(o):
        if hasattr(o, 'isoformat'):
            return o.isoformat()
        if isinstance(o, Enum):
            return o.value
        else:
            json.JSONEncoder.default(str(o), o)

    def to_json(self):
        return json.loads(json.dumps(self.dict(), default=self.default),
                          # sort_keys=True,
                          # indent=1,
                          )

    def get_base(self):
        return {
            'alt_id': self.dealId or self.recId,
            'insert_date': self.docDate,

            'scenario': " ",

            'purpose': self.purpose,
            'currency': self.iso,
            'amount': self.amount,
            'amount_to_gel': self.amountEqu
        }

    def get_deal(self):
        return {
            'DealType': self.transactionType.value,
            'DealForm': self.dealform,
            'Participate': self.participate.fullName or \
                           f"{self.participate.firstName} {self.participate.lastName}" if \
                self.participate else "ძველი მონაცემია"
            ,
        }

    def get_transaction(self):
        return {
            'transactionType': self.transactionType.value,
            'debitorBank': self.debit.bankName,
            'creditorBank': self.credit.bankName,
            'debitorAccount': self.debit.accountNumber,
            'creditorAccount': self.credit.accountNumber,
            'creditor': self.credit.fullName or f"{self.credit.firstName} {self.credit.lastName}",
            'debitor': self.debit.fullName or f"{self.debit.firstName} {self.debit.lastName}",
        }
