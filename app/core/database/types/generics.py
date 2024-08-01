from typing import TypeVar

from app.core.database.models import Model


__all__ = (
    '_MT',
)


_MT = TypeVar('_MT', bound=Model)
