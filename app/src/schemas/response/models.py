from typing import  Union

from pydantic import BaseModel

from app.src.schemas.response.enums.types import TransactionCreationStatus


class TransactionCreationResponse(BaseModel):
    status: TransactionCreationStatus
