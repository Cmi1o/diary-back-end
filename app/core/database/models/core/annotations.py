from typing import Annotated
from datetime import datetime

from sqlalchemy import (
    String, 
    DateTime,
)
from sqlalchemy.orm import mapped_column


__all__ = (
    'str255', 
    'str50', 
    'integer', 
    'time'
)


str50 = Annotated[str, mapped_column(String(50))]
str255 = Annotated[str, mapped_column(String(255))] # string with a max length of 255
integer = Annotated[int, mapped_column()]
time = Annotated[datetime, mapped_column(DateTime())]
