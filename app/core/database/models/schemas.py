from typing import List

from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

from app.core.database.types import Role
from .core import Model
from .core.annotations import *


class User(Model):
    name: Mapped[str50]
    email: Mapped[str50]
    salt: Mapped[str100]
    # will use SHA256 hash
    # password_and_salt_hash = SHA256(password + salt)
    password_and_salt_hash: Mapped[str100]
    role: Mapped[Role] = mapped_column(Enum(Role))
    
    tasks: Mapped[List['Task']] = relationship(back_populates='user', lazy='selectin')


class Task(Model):
    name: Mapped[str50]
    description: Mapped[str255]
    
    user_id: Mapped[integer] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship(back_populates='tasks', lazy='selectin')
