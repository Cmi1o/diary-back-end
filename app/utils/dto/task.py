from pydantic import BaseModel
from .user import UserDto


class TaskDto(BaseModel):
    name: str
    description: str
    user_id: int
    user: UserDto
