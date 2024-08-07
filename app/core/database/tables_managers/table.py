from typing import AsyncGenerator
from sqlalchemy import sql

from app.core.database.models import Model
from app.core.database.models.core import session_factory

from .base import ITableManager


class Table[_MT: Model](ITableManager[_MT]):
    def __init__(self, table: _MT) -> None:
        self.__table = type(table)
    
    async def get_by(self, **filter_data):
        async with session_factory() as session:
            return await session.scalar(
                sql.select(self.__table).filter_by(
                    **filter_data
                )
            )
    
    async def get_all(self) -> AsyncGenerator[_MT, None]:
        async with session_factory() as session:
            stmt = sql.select(self.__table)
            async for row in await session.stream(stmt):
                yield row[0]
    
    async def get_many_with(self, **filter_data) -> AsyncGenerator[_MT, None]:
        async with session_factory() as session:
            stmt = sql.select(self.__table).filter_by(**filter_data)
            async for row in await session.stream(stmt):
                yield row[0]
    
    async def create(self, **data):
        async with session_factory() as session:
            session.add(self.__table(**data))
            await session.commit()
    
    async def update_by(self, values, **filter_data):
        async with session_factory() as session:
            stmt = sql.update(self.__table).filter_by(**filter_data)
            
            await session.execute(stmt.values(**values))
            await session.commit()
    
    async def delete_by(self, **filter_data):
        async with session_factory() as session:
            stmt = sql.delete(self.__table).filter_by(**filter_data)
            
            await session.execute(stmt)
            await session.commit()
