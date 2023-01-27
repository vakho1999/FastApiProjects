from sqlalchemy import Integer, String, ForeignKey, DateTime, Text
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship

from app.src.models.Base import DateTimeClass

from app.src.schemas.requests.TransactionApiSchema import TransactionApiSchema


class BaseDataOperation(DateTimeClass):
    __abstract__ = True
    insert_date = Column(DateTime(timezone=True))
    alt_id = Column(String(length=20), nullable=False)
    scenario = Column(String(length=100), nullable=False)
    purpose = Column(String(length=100), nullable=False)
    extra_purpose = Column(Text(), nullable=True)
    currency = Column(String(length=5), nullable=False)
    amount = Column(Integer, nullable=False)
    amount_to_gel = Column(Integer, nullable=False)


class Transaction(BaseDataOperation):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, autoincrement=True)
    detail = relationship("StructuredTransaction", backref="transaction", cascade="all, delete, delete-orphan", lazy=True, uselist=False)
    transactionType = Column(String(length=20), nullable=False)
    debitorBank = Column(String(length=30), nullable=False)
    creditorBank = Column(String(length=30), nullable=False)
    debitorAccount = Column(String(length=30), nullable=False)
    creditorAccount = Column(String(length=30), nullable=False)
    creditor = Column(String(length=30), nullable=False)
    debitor = Column(String(length=30), nullable=False)

    def __init__(self, data: TransactionApiSchema):
        super(BaseDataOperation, self).__init__(**data.get_base())
        self.__dict__.update(data.get_transaction())




class Deal(BaseDataOperation):
    __tablename__ = "deal"

    id = Column(Integer, primary_key=True, autoincrement=True)
    detail = relationship("StructuredTransaction", backref="deal", cascade="all, delete, delete-orphan", lazy=True, uselist=False)
    DealType = Column(String(length=30), nullable=False)
    DealForm = Column(String(length=30), nullable=False)
    Participate = Column(String(length=30), nullable=False)

    def __init__(self, data: TransactionApiSchema):
        super(BaseDataOperation, self).__init__(**data.get_base())
        self.__dict__.update(data.get_deal())

class StructuredTransaction(DateTimeClass):
    __tablename__ = "structured_transaction"

    id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_id = Column(Integer, ForeignKey('transaction.id', ondelete='CASCADE'), nullable=True)
    deal_id = Column(Integer, ForeignKey('deal.id', ondelete='CASCADE'), nullable=True)
    data = Column(JSONB, default={})


class DealFilters(DateTimeClass):
    __tablename__ = "deal_filters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(UUID(as_uuid=True), nullable=False)
    data = Column(JSONB, default={})

class TransactionFilters(DateTimeClass):
    __tablename__ = "transaction_filters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(UUID(as_uuid=True), nullable=False)
    data = Column(JSONB, default={})

class TransactionTableSettings(DateTimeClass):
    __tablename__ = "user_transaction_table_settings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(UUID(as_uuid=True), nullable=False)
    data = Column(JSONB, default={})

class DealTableSettings(DateTimeClass):
    __tablename__ = "user_deal_table_settings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(UUID(as_uuid=True), nullable=False)
    data = Column(JSONB, default={})


