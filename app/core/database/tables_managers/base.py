from abc import ABC, abstractmethod
from typing import Any, AsyncGenerator

from app.core.database.models import Model


class ITableManager[_MT: Model](ABC):
    def __init__(self, **__negative_settings__: Any) -> None: ...
    
    @abstractmethod
    async def get_all(self) -> AsyncGenerator[_MT, None]:
        '''_summary_
        
        Returns
        -------
        AsyncGenerator[Model, None]
            _description_
        '''

    @abstractmethod
    async def get_many_with(self, **filter_data) -> AsyncGenerator[_MT, None]:
        '''_summary_
        
        Returns
        -------
        AsyncGenerator[_AT, None]
            _description_
        '''
    
    @abstractmethod
    async def get_by(self, **filter_data) -> _MT:
        '''_summary_
        
        Returns
        -------
        _AT
            _description_
        '''
    
    @abstractmethod
    async def update_by(self, **filter_data) -> ...:
        '''_summary_
        
        Returns
        -------
        _AT
            _description_
        '''
    
    @abstractmethod
    async def delete_by(self, **filter_data) -> None:
        '''_summary_
        
        Returns
        -------
        None
            _description_
        '''
    
    @abstractmethod
    async def create(self, **data) -> None:
        '''_summary_
        
        Returns
        -------
        None
            _description_
        '''
