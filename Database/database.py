import sqlite3
from datetime import datetime

DB_NAME = "bot_users.db"

def init_db():
 
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        first_name TEXT,
        username TEXT,
        joined_at TEXT,
        last_seen TEXT
    )
    """)
    conn.commit()
    conn.close()

def save_user_to_db(user_id, first_name, username):
    """Insert or update user info in database"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    now = datetime.now().isoformat()

    cursor.execute("""
    INSERT OR REPLACE INTO users (user_id, first_name, username, joined_at, last_seen)
    VALUES (?, ?, ?, COALESCE((SELECT joined_at FROM users WHERE user_id=?), ?), ?)
    """, (user_id, first_name, username, user_id, now, now))

    conn.commit()
    conn.close()
