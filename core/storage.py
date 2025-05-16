import json
from core.models import Credential
from core.encryption import encrypt_data, decrypt_data

DATA_FILE = "resources/data.enc"

def save_credentials(credentials: list[Credential]):
    json_data = json.dumps([cred.__dict__ for cred in credentials])
    encrypted = encrypt_data(json_data)
    with open(DATA_FILE, "wb") as f:
        f.write(encrypted)

def load_credentials() -> list[Credential]:
    try:
        with open(DATA_FILE, "rb") as f:
            encrypted = f.read()
        decrypted = decrypt_data(encrypted)
        data = json.loads(decrypted)
        return [Credential(**item) for item in data]
    except FileNotFoundError:
        return []
    except Exception as e:
        print("Error decrypting:", e)
        return []