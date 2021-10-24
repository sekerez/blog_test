import secrets

def generate_key() -> str:
    return secrets.token_hex()
