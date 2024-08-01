from sqlalchemy.orm import Mapped

from .core import Base
from .core.annotations import *


class Task(Base):
    name: Mapped[str50]
    description: Mapped[str255]
