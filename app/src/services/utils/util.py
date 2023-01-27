import datetime
import re

from pydantic.types import date
from sqlalchemy import not_


def is_datetime(string: date):
    # iso_8601_datetime_regex = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{3})?Z$"
    iso_8601_datetime_regex = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}"
    if re.match(iso_8601_datetime_regex, str(string)):
        return True
    return False


def filter_transaction(self, field, value):
    value = value["value"]
    instance = self._get_instance("data")
    if is_datetime(value): value = datetime.datetime.fromisoformat(value)

    if (not isinstance(value, str) or is_datetime(value)) and \
            not field.endswith("_eq") and \
            not field.endswith("_not_eq"):
        if field.endswith("_end"):
            self.query = self.query.filter(instance.__dict__[field.replace("_end", "")] <= value)
            return
        self.query = self.query.filter(instance.__dict__[field.replace("_start", "")] >= value)
        return
    elif field.endswith("_not_in"):
        self.query = self.query.filter(not_(instance.__dict__[field.replace("_not_in", "")].ilike(f"%{value}%")))
        return
    elif field.endswith("_in"):
        self.query = self.query.filter(instance.__dict__[field.replace("_in", "")].ilike(f"%{value}%"))
        return
    elif field.endswith("_not_eq"):
        self.query = self.query.filter(instance.__dict__[field.replace("_not_eq", "")] != value)
        return
    self.query = self.query.filter(instance.__dict__[field.replace("_eq", "")] == value)
