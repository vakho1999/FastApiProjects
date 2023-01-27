from typing import Optional

from pydantic import BaseModel
from pydantic.class_validators import Any
from pydantic.validators import datetime, date


class BasePageField(BaseModel):
    id: Optional[int]
    insert_date: Optional[datetime]
    alt_id: Optional[str]
    scenario: Optional[str]
    purpose: Optional[str]
    currency: Optional[str]
    amount: Optional[int]
    amount_to_gel: Optional[int]

    class Config:
        orm_mode = True


class BaseFilter(BaseModel):
    # insert_date: Optional[date]
    alt_id: Optional[dict[str,Any]] = {"value": "", "name": "აიდი", "operator": ""}
    insert_date_end: Optional[dict[str,Any]] = {"value": "", "name": "თარიღამდე", "operator": ""}
    insert_date_start: Optional[dict[str,Any]] = {"value": "", "name": "თარიღიდან", "operator": ""}
    insert_date_eq: Optional[dict[str,Any]] = {"value": "", "name": "თარიღი უდრის", "operator": ""}
    insert_date_not_eq: Optional[dict[str,Any]] = {"value": "", "name": "თარიღი არ უდრის", "operator": ""}
    purpose_in: Optional[dict[str,Any]] = {"value": "", "name": "დანიშნულება შეიცავს", "operator": ""}
    purpose_not_in: Optional[dict[str,Any]] = {"value": "", "name": "დანიშნულება არ შეიცავს", "operator": ""}
    purpose_eq: Optional[dict[str,Any]] = {"value": "", "name": "დანიშნულება უდრის", "operator": ""}
    purpose_not_eq: Optional[dict[str,Any]] = {"value": "", "name": "დანიშნულება არ უდრის", "operator": ""}
    extra_purpose_in: Optional[dict[str,Any]] = {"value": "", "name": "დამატებითი შეიცავს", "operator": ""}
    extra_purpose_not_in: Optional[dict[str,Any]] = {"value": "", "name": "დამატებითი არ შეიცავს", "operator": ""}
    extra_purpose_eq: Optional[dict[str,Any]] = {"value": "", "name": "დამატებითი უდრის", "operator": ""}
    extra_purpose_not_eq: Optional[dict[str,Any]] = {"value": "", "name": "დამატებითი არ უდრის", "operator": ""}
    amount_end: Optional[dict[str,Any]] = {"value": "", "name": "თანხამდე", "operator": ""}
    amount_start: Optional[dict[str,Any]] = {"value": "", "name": "თანხიდან", "operator": ""}
    amount_eq: Optional[dict[str,Any]] = {"value": "", "name": "თანხა უდრის", "operator": ""}
    amount_not_eq: Optional[dict[str,Any]] = {"value": "", "name": "თანხა არ უდრის", "operator": ""}
    amount_to_gel_end: Optional[dict[str,Any]] = {"value": "", "name": "ექვივალენტი თანხამდე", "operator": ""}
    amount_to_gel_eq: Optional[dict[str,Any]] = {"value": "", "name": "ექვივალენტი თანხა უდრის", "operator": ""}
    amount_to_gel_start: Optional[dict[str,Any]] = {"value": "", "name": "ექვივალენტი თანხიდან", "operator": ""}
    amount_to_gel_not_eq: Optional[dict[str,Any]] = {"value": "", "name": "ექვივალენტი თანხა არ უდრის", "operator": ""}


class DealPage(BasePageField):
    DealType: Optional[str]
    DealForm: Optional[str]
    Participate: Optional[str]


class TransactionPage(BasePageField):
    transactionType: Optional[str]
    debitorBank: Optional[str]
    creditorBank: Optional[str]
    debitorAccount: Optional[str]
    creditorAccount: Optional[str]
    creditor: Optional[str]
    debitor: Optional[str]



class TransactionPageFilter( BaseFilter):
    creditor_in: Optional[dict[str,Any]] = {"value": "", "name": "კრედიტორი შეიცავს", "operator": ""}
    creditor_not_in: Optional[dict[str,Any]] = {"value": "", "name": "კრედიტორი არ შეიცავს", "operator": ""}
    creditor_eq: Optional[dict[str,Any]] = {"value": "", "name": "კრედიტორი უდრის", "operator": ""}
    creditor_not_eq: Optional[dict[str,Any]] = {"value": "", "name": "კრედიტორი არ უდრის", "operator": ""}
    creditorBank_in: Optional[dict[str,Any]] = {"value": "", "name": "კრედიტორის ბანკი შეიცავს", "operator": ""}
    creditorBank_not_in: Optional[dict[str,Any]] = {"value": "", "name": "კრედიტორის ბანკი არ შეიცავს", "operator": ""}
    creditorBank_eq: Optional[dict[str,Any]] = {"value": "", "name": "კრედიტორის ბანკი უდრის", "operator": ""}
    creditorBank_not_eq: Optional[dict[str,Any]] = {"value": "", "name": "კრედიტორის ბანკი არ უდრის", "operator": ""}
    debitor_in:  Optional[dict[str,Any]] = {"value": "", "name": "დებიტორი შეიცავს", "operator": ""}
    debitor_not_in: Optional[dict[str,Any]] = {"value": "", "name": "დებიტორი არ შეიცავს", "operator": ""}
    debitor_eq: Optional[dict[str,Any]] = {"value": "", "name": "დებიტორი უდრის", "operator": ""}
    debitor_not_eq: Optional[dict[str,Any]] = {"value": "", "name": "დებიტორი არ უდრის", "operator": ""}
    debitorBank_in: Optional[dict[str,Any]] = {"value": "", "name": "დებიტორის ბანკი შეიცავს", "operator": ""}
    debitorBank_not_in: Optional[dict[str,Any]] = {"value": "", "name": "დებიტორის ბანკი არ შეიცავს", "operator": ""}
    debitorBank_eq: Optional[dict[str,Any]] = {"value": "", "name": "დებიტორის ბანკი უდრის", "operator": ""}
    debitorBank_not_eq: Optional[dict[str,Any]] = {"value": "", "name": "დებიტორის ბანკი არ უდრის", "operator": ""}
    transactionType_eq: Optional[dict[str,Any]] = {"value": "", "name": "ტრანზაქციის ტიპი უდრის", "operator": ""}
    transactionType_not_eq: Optional[dict[str,Any]] = {"value": "", "name": "ტრანზაქციის ტიპი არ უდრის", "operator": ""}

class DealPageFilter(BaseFilter):
    DealType_in: Optional[dict[str,Any]] = {"value": "", "name": "გარიგების ტიპი შეიცავს", "operator": ""}
    DealType_not_in: Optional[dict[str,Any]] = {"value": "", "name": "გარიგების ტიპი არ შეიცავს", "operator": ""}
    DealType_eq: Optional[dict[str,Any]] = {"value": "", "name": "გარიგების ტიპი უდრის", "operator": ""}
    DealType_not_eq: Optional[dict[str,Any]] = {"value": "", "name": "გარიგების ტიპი არ უდრის", "operator": ""}
    DealForm_in: Optional[dict[str,Any]] = {"value": "", "name": "გარიგების ფორმა შეიცავს", "operator": ""}
    DealForm_not_in: Optional[dict[str,Any]] = {"value": "", "name": "გარიგების ფორმა არ შეიცავს", "operator": ""}
    DealForm_eq: Optional[dict[str,Any]] = {"value": "", "name": "გარიგების ფორმა არ უდრის", "operator": ""}
    DealForm_not_eq: Optional[dict[str,Any]] = {"value": "", "name": "გარიგების ფორმა არ უდრის", "operator": ""}
    Participate_not_in: Optional[dict[str,Any]] = {"value": "", "name": "მონაწილე პირი არ შეიცავს", "operator": ""}
    Participate_in: Optional[dict[str,Any]] = {"value": "", "name": "მონაწილე პირი შეიცავს", "operator": ""}
    Participate_eq: Optional[dict[str,Any]] = {"value": "", "name": "მონაწილე პირი უდრის", "operator": ""}
    Participate_not_eq: Optional[dict[str,Any]] = {"value": "", "name": "მონაწილე პირი არ უდრის", "operator": ""}
