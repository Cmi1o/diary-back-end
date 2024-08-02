from pydantic import BaseModel, EmailStr
from app.core.database.types import Role


class UserDto(BaseModel):
    name: str
    email: EmailStr
    password_hash: int
    salt_hash: int
    role: Role
