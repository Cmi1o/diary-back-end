from sqlalchemy.orm import Mapped

from .core import Model
from .core.annotations import *


class User(Model):
    name: Mapped[str50]
    password: Mapped[integer]
    salt_hash: Mapped[integer]


class Task(Model):
    name: Mapped[str50]
    description: Mapped[str255]
