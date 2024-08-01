from .session_factory import session_factory
from .base import Base


class Model(Base):
    __abstract__ = True
