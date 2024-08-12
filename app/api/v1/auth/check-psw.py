from app.core.database import controller
from crypto import hash


async def validate_psw(user, psw):
    db_user = await controller.users.get_by(name=user)
    if not db_user:
        raise ValueError("User not found")
    user_psw_hash = db_user.password_hash
    user_salt = db_user.salt
    
    if user_psw_hash != hash(user_salt + psw):
        raise ValueError("Incorrect password")
    
    
    
    