from pydantic import BaseModel, EmailStr, field_validator


class AuthUserDTO(BaseModel):
    name: str
    email: EmailStr
    password: str
    
    @field_validator('password')
    def validate_password(cls, password: str):
        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return password
