from abc import ABC, abstractmethod

from fastapi_pagination.bases import AbstractPage

from app.src.models.Transaction import Transaction


class UserSettingInterface(ABC):

    # @abstractmethod
    # def get_all_transactions(self) -> None:
    #     """ retrieve all transaction records, Pagination should be by default """
    #
    #     ...

    @abstractmethod
    def get_user_specific_setting(self, user: str) -> None:
        """ retrieve user related setting"""
        ...

    @abstractmethod
    def execute(self) -> AbstractPage[Transaction]:
        ...