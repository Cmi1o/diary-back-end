from pydantic import BaseModel, EmailStr, field_validator


class AuthUserDTO(BaseModel):
    login: str
    email: EmailStr
    password: str
    
    
    @field_validator('login')
    def validate_login(cls, login: str):
        if (len(login) < 5):
            raise ValueError("Login must be at least 5 characters long")
        return login
        
    
    @field_validator('password')
    def validate_password(cls, password: str):
        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return password
