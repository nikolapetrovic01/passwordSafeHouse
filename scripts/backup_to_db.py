import mysql.connector
print("USING mysql.connector FROM:", mysql.connector.__file__)
from datetime import datetime
import os

# --- Config ---
DB_CONFIG = {
    "host": "localhost",
    "user": "nikola",
    "password": "nik123",
    "database": "passwordSafeHouse"
}

DATA_FILE = "resources/data.enc"

# --- Read encrypted file ---
if not os.path.exists(DATA_FILE):
    print("No file found")
    exit(1)

with open(DATA_FILE, "rb") as f:
    encrypted_data = f.read()

try:
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    query = "INSERT INTO backups (timestamp, data) VALUES (%s,%s)"
    cursor.execute(query, (datetime.now(), encrypted_data))
    conn.commit()

    cursor.close()
    conn.close()
except mysql.connector.Error as error:
    print(f"Database error: {error}")