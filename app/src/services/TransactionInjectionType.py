import json
from typing import Union
from uuid import UUID

from sqlalchemy.orm import Session

from app.src.db.utils import update_jsonb
from app.src.models.Transaction import StructuredTransaction, Transaction, Deal, TransactionFilters, DealFilters, \
    TransactionTableSettings, DealTableSettings

from app.src.schemas.requests.TransactionApiSchema import TransactionApiSchema
from app.src.schemas.requests.TransactionPageSchema import TransactionPageFilter, DealPageFilter
from app.src.schemas.requests.TransactionSettings import DealSettings, TransactionSettings
from app.src.services.interfaces.TransactionInterface import TrasactionDataInjectionServiceImpl


class DataTableInjection(TrasactionDataInjectionServiceImpl):

    @classmethod
    def save(cls, instance: Union[tuple[TransactionTableSettings, None],
                                  tuple[DealTableSettings, None]], data: TransactionSettings | DealSettings, session: Session,
             user: UUID = None):

        instance, *_ = instance
        if already_exist := session.query(instance).filter_by(uid=user).first():
            already_exist.data = json.loads(data.json())
            update_jsonb(already_exist, "data", session)
            return
        instance = instance(data=data.dict(), uid=user)

        session.add(instance)
        session.commit()


class TransactionInjection(TrasactionDataInjectionServiceImpl):

    @classmethod
    def save(cls, instance: Union[tuple[Transaction, TransactionFilters],
                                  tuple[Deal, DealFilters]], data: TransactionApiSchema, session: Session,
             user: UUID = None):
        transaction: StructuredTransaction = StructuredTransaction(data=data.to_json())
        instance, *_ = instance
        instance = instance(data)
        instance.detail = transaction

        session.add(instance)
        session.commit()

class TransactionInjection(TrasactionDataInjectionServiceImpl):

    @classmethod
    def save(cls, instance: Union[tuple[Transaction, TransactionFilters],
                                  tuple[Deal, DealFilters]], data: TransactionApiSchema, session: Session,
             user: UUID = None):
        instance_, *_ = instance
        instance = instance_(data)
        if session.query(instance_).filter_by(alt_id=instance_.alt_id).first():
            return

        transaction: StructuredTransaction = StructuredTransaction(data=data.to_json())

        instance.detail = transaction

        session.add(instance)
        session.commit()


class TransactionFiltersInjection(TrasactionDataInjectionServiceImpl):

    @classmethod
    def save(cls, instance: Union[tuple[Transaction, TransactionFilters],
                                  tuple[Deal, DealFilters]], data: TransactionPageFilter | DealPageFilter, session: Session,
             user: UUID = None):
        *_, instance = instance
        if already_exist := session.query(instance).filter_by(uid=user).first():
            already_exist.data = json.loads(data.json())
            update_jsonb(already_exist, "data", session)
            return
        instance: DealFilters | TransactionFilters = instance(data=json.loads(data.json()), uid=user)
        session.add(instance)
        session.commit()
