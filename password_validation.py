import string


def validate_password(password: str) -> bool:
    if all([len(password) >= 8,
            any(char.isdigit() for char in password),
            any(char.islower() for char in password),
            any(char.isupper() for char in password),
            " " not in password,
            any(char in string.punctuation for char in password),
            password.isascii()]):
        return True
    return False
