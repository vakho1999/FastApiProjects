from app.src.db.database import Base
from sqlalchemy import func, DateTime, Column


class DateTimeClass(Base):
    __abstract__ = True

    created_on = Column(DateTime(timezone=True), default=func.now())

    # updated_on = Column(DateTime, default=func.now(), onupdate=func.now())
