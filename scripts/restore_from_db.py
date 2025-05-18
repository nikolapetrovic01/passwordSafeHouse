import mysql.connector
import os

# --- Config ---
DB_CONFIG = {
    "host": "localhost",
    "user": "nikola",
    "password": "nik123",
    "database": "passwordSafeHouse"
}

DATA_FILE = "resources/data.enc"

# --- Connect to database ---
try:
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    #Fetch latest backup
    cursor.execute("SELECT * FROM backups ORDER BY timestamp DESC LIMIT 1")
    result = cursor.fetchone()

    if result is None:
        # TODO: Make a notification 
        print("No backups found")
    else:
        encrypted_data = result[2]
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "wb") as f:
            f.write(encrypted_data)
        print("✅ Restored data.enc from latest backup.")

    cursor.close()
    conn.close()
except mysql.connector.Error as err:
    print(f"Database error: {err}")
