import secrets


def generate_id():
    return str(secrets.token_hex())[:16]
