import random
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


def generate_answer() -> dict:
    greating_patterns = [
        "Hello there!",
        "Hi! How can I help you?",
        "Greetings!",
        "Hey! What's up?",
    ]
    message = f'{random.choice(greating_patterns)}, User'
    return {"message": message, "status": "ok"}


def hash_password(password: str) -> str:
    ph = PasswordHasher()
    password_hash = ph.hash(password)
    ph.verify(password_hash, password)

    return ph.hash(password)


