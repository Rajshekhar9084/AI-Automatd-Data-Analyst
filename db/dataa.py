from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).parent / "app.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS api_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT
        )
    """)

    conn.commit()
    conn.close()