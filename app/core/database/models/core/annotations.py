from enum import Enum, auto
from typing import Annotated
from datetime import datetime

from sqlalchemy import (
    String, 
    DateTime
)
from sqlalchemy.orm import mapped_column


__all__ = (
    'str255', 
    'str50', 
    'integer', 
    'time',
    'Role'
)


class Role(Enum):
    admin = auto()
    user = auto()


str255 = Annotated[str, mapped_column(String(255))] # string with a max length
str50 = Annotated[str, mapped_column(String(50))]
integer = Annotated[int, mapped_column()]
time = Annotated[datetime, mapped_column(DateTime())]
