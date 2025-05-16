import json
from core.models import Credential

DATA_FILE = "resources/data.json"

def save_credentials(credentials: list[Credential]):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([cred.__dict__ for cred in credentials], f)

def load_credentials() -> list[Credential]:
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Credential(**item) for item in data]
    except FileNotFoundError:
        return []