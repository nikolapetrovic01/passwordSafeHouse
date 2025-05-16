from cryptography.fernet import Fernet
import os

APP_NAME = "PasswordSafeHouse"
KEY_FILENAME = "key.key"

def get_key_path() -> str:
    base = os.getenv('LOCALAPPDATA') or os.path.expanduser("~/.local/share")
    path = os.path.join(base, APP_NAME)
    os.makedirs(path, exist_ok = True)
    return os.path.join(path, KEY_FILENAME)

def load_or_create_key() -> bytes:
    key_path = get_key_path()

    if os.path.exists(key_path):
        with open(key_path, "rb") as f:
            return f.read()
    
    # First run: generate and save key
    key = Fernet.generate_key()
    with open(key_path, "wb") as f:
        f.write(key)
    return key

def encrypt_data(data: str) -> bytes:
    return Fernet(load_or_create_key()).encrypt(data.encode("utf-8"))

def decrypt_data(token: bytes) -> str:
    return Fernet(load_or_create_key()).decrypt(token).decode("utf-8")