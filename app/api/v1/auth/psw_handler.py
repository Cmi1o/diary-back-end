from app.core.database import controller
import secrets
from hashlib import sha256


def hash(message: str) -> str:
    return sha256(message.encode()).hexdigest()


# saves psw and salt to db
async def update_psw(user, new_psw: str):
    # fetch user by name
    db_user = await controller.users.get_by(name=user) 
    if not db_user:
        raise ValueError(f"User {user} not found")
    
    # create salt and psw hash
    salt = secrets.token_urlsafe(len(new_psw))  # string of random len(psw) bytes in Base64
    user_psw_hash = hash(salt + new_psw), salt
    
    # save to db
    db_user.password_hash = user_psw_hash
    db_user.salt = salt
    

# fetches user from db, checks input psw with saved psw
async def validate_psw(user, psw: str) -> bool:
    db_user = await controller.users.get_by(name=user)
    if not db_user:
        raise ValueError(f"User {user} not found")
    
    user_psw_hash = db_user.password_hash
    user_salt = db_user.salt
    
    return secrets.compare_digest(user_psw_hash, hash(user_salt + psw))  # timing attack safe
