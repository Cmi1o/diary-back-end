from sqlalchemy import sql

from app.core.database.models import Model
from app.core.database.models.core import session_factory

from .base import ITableManager


class Table[_MT: Model](ITableManager[_MT]):
    def __init__(self, table, **negative_settings) -> None:
        self.table = type(table)
    
    async def get_by(self, **filter_data):
        async with session_factory() as session:
            return await session.scalar(
                sql.select(self.table).filter_by(
                    **filter_data
                )
            )
