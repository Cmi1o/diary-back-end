from abc import ABC, abstractmethod
from typing import Any, AsyncGenerator

from app.core.database.models import Model


class ITableManager[_MT: Model](ABC):
    @abstractmethod
    def __init__(self, **negative_settings: Any) -> None: ...
    
    @abstractmethod
    async def get_all(self) -> AsyncGenerator[_MT, None]:
        '''Asynchronous generator for getting all rows from table
        
        Yields
        -------
        Table row data
        '''

    @abstractmethod
    async def get_many_with(self, **filter_data) -> AsyncGenerator[_MT, None]:
        '''Asynchronous generator for getting rows from table with filter data
        
        Parameters
        ----------
        filter_data : ...
        
        Yields
        -------
        Table row data
        '''
    
    @abstractmethod
    async def get_by(self, **filter_data) -> _MT | None:
        '''Asynchronous method for getting row from table by `filter_data`
        
        Parameters
        ----------
        filter_data : ...
        
        Returns
        -------
        table row | None
        '''
    
    @abstractmethod
    async def update_by(self, **filter_data) -> ...:
        '''...
        
        Parameters
        ----------
        filter_data : ...
        
        Returns
        -------
        '''
    
    @abstractmethod
    async def delete_by(self, **filter_data) -> None:
        '''Asynchronous method for deleting row from table by `filter_data`
        
        Parameters
        ----------
        filter_data : ...
        '''
    
    @abstractmethod
    async def create(self, **data) -> None:
        '''Asynchronous method for creating new row in table
        
        Parameters
        ----------
        data : ...
        '''
