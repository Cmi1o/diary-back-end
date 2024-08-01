from sqlalchemy.orm import Mapped

from .core.annotations import *
from .core import Base


class User(Base):
    name: Mapped[str50]
    password: Mapped[integer]
    salt_hash: Mapped[integer]
