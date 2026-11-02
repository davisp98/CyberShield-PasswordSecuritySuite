import secrets
import string


def generate_password(length, uppercase, lowercase, numbers, symbols):

    characters = ""

    if uppercase:
        characters += string.ascii_uppercase

    if lowercase:
        characters += string.ascii_lowercase

    if numbers:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    if not characters:
        return ""

    password = []

    if uppercase:
        password.append(secrets.choice(string.ascii_uppercase))

    if lowercase:
        password.append(secrets.choice(string.ascii_lowercase))

    if numbers:
        password.append(secrets.choice(string.digits))

    if symbols:
        password.append(secrets.choice(string.punctuation))

    if length < len(password):
        return ""

    while len(password) < length:
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)