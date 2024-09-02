from app.core.database import controller
from ..additional_crypto import hash
import secrets


# fetches user from db, checks input psw with saved psw
async def validate_psw(user, psw: str):
    db_user = await controller.users.get_by(name=user)
    if not db_user:
        raise ValueError("User not found")
    
    user_psw_hash = db_user.password_hash
    user_salt = db_user.salt
    
    if secrets.compare_digest(user_psw_hash, hash(user_salt + psw)):  # timing attack safe
        raise ValueError("Incorrect password")
    
