from argon2 import PasswordHasher


def hash_password(password: str) -> str:
    ph = PasswordHasher()
    password_hash = ph.hash(password)
    ph.verify(password_hash, password)

    return ph.hash(password)