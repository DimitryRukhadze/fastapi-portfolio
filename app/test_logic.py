import random


def generate_answer() -> dict:
    greating_patterns = [
        "Hello there!",
        "Hi! How can I help you?",
        "Greetings!",
        "Hey! What's up?",
    ]
    message = f'{random.choice(greating_patterns)}, User'
    return {"message": message, "status": "ok"}