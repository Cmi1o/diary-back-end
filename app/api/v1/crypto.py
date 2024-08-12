from hashlib import sha256


def hash(message: str) -> str:
    return sha256(message.encode()).hexdigest()


