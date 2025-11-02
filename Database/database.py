import sqlite3
from datetime import datetime

DB_NAME = "bot_users.db"

def init_db():
    """Initialize the database with all required tables"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        first_name TEXT,
        username TEXT,
        joined_at TEXT,
        last_seen TEXT,
        total_interactions INTEGER DEFAULT 0,
        current_state TEXT DEFAULT 'main_menu'
    )
    """)
    
    # Sessions table for tracking active sessions
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessions (
        session_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        start_time TEXT,
        last_activity TEXT,
        state TEXT,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )
    """)
    
    # User interactions log
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interactions (
        interaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        action_type TEXT,
        timestamp TEXT,
        details TEXT,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )
    """)
    
    conn.commit()
    conn.close()

def save_user_to_db(user_id, first_name, username):
    """Insert or update user info and increment interactions"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    now = datetime.now().isoformat()

    cursor.execute("""
    INSERT OR REPLACE INTO users 
    (user_id, first_name, username, joined_at, last_seen, total_interactions)
    VALUES (?, ?, ?, 
            COALESCE((SELECT joined_at FROM users WHERE user_id=?), ?),
            ?,
            COALESCE((SELECT total_interactions FROM users WHERE user_id=?), 0) + 1
    )
    """, (user_id, first_name, username, user_id, now, now, user_id))

    conn.commit()
    conn.close()

def log_interaction(user_id, action_type, details=""):
    """Log each user interaction"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    now = datetime.now().isoformat()
    
    cursor.execute("""
    INSERT INTO interactions (user_id, action_type, timestamp, details)
    VALUES (?, ?, ?, ?)
    """, (user_id, action_type, now, details))
    
    # Update user's last_seen
    cursor.execute("""
    UPDATE users SET last_seen = ?, total_interactions = total_interactions + 1
    WHERE user_id = ?
    """, (now, user_id))
    
    conn.commit()
    conn.close()

def update_user_state(user_id, state):
    """Update user's current state"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    now = datetime.now().isoformat()
    
    cursor.execute("""
    UPDATE users SET current_state = ?, last_seen = ?
    WHERE user_id = ?
    """, (state, now, user_id))
    
    conn.commit()
    conn.close()

