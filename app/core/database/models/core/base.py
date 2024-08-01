from sqlalchemy.orm import (
    mapped_column,
    DeclarativeBase,
    Mapped, declared_attr
)
from sqlalchemy.ext.asyncio import AsyncAttrs

from .annotations import time


class Base(AsyncAttrs, DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[time]
    updated_at: Mapped[time]
    
    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}s'
