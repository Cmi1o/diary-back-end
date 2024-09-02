import secrets

from hashlib import sha256

from app.core.database import controller


def hash(message: str) -> str:
    return sha256(message.encode()).hexdigest()


# saves psw and salt to db
async def update_psw(user_name: str, new_psw: str) -> None:
    # fetch user by name
    user = await controller.users.get_by(name=user_name) 
    if not user:
        raise ValueError(f'User {user_name} not found')
    
    # create salt and psw hash
    salt = secrets.token_urlsafe(len(new_psw))  # string of random len(psw) bytes in Base64
    user_psw_hash = hash(salt + new_psw)
    
    await controller.users.update_by(name=user_name, values={
        'password_hash': user_psw_hash,
        'salt': salt
    })


# fetches user from db, checks input psw with saved psw
async def validate_psw(user_name: str, psw: str) -> bool:
    user = await controller.users.get_by(name=user_name)
    if not user:
        raise ValueError(f'User {user_name} not found')
    
    # timing attack safe
    return secrets.compare_digest(
        user.password_hash, hash(user.salt + psw)
    )  
