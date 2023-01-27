from enum import Enum

from starlette import status


class HttpStatusCodes(int, Enum):
    CREATED = status.HTTP_201_CREATED
    PROGRAMMING_ERROR = status.HTTP_500_INTERNAL_SERVER_ERROR
    LOGICAL_ERROR = status.HTTP_409_CONFLICT
    UNAUTHORIZED = status.HTTP_401_UNAUTHORIZED
    OK = status.HTTP_200_OK


class TransactionCreationStatus(int, Enum):
    PROGRAMMING_ERROR = status.HTTP_500_INTERNAL_SERVER_ERROR
    CREATED = status.HTTP_201_CREATED

    @classmethod
    def get_member(cls):
        return cls._member_names_

    @classmethod
    def __get_validators__(cls):
        cls.lookup = {v: k.value for v, k in cls.__members__.items()}
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            return cls.lookup[v]
        except KeyError:
            raise ValueError('invalid value')