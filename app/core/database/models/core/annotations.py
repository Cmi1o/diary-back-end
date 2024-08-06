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
    'str100'
)


str255 = Annotated[str, mapped_column(String(255))] # string with a max length
str50 = Annotated[str, mapped_column(String(50))]
str100 = Annotated[str, mapped_column(String(100))]
integer = Annotated[int, mapped_column()]
time = Annotated[datetime, mapped_column(DateTime())]
