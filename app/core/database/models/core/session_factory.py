from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine 
)

from app.config import database_url


_engine = create_async_engine(url=database_url, echo=False)
session_factory = async_sessionmaker(
    bind=_engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)
