import sqlite3
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
import os
from datetime import datetime

DATABASE = os.environ.get('DATABASE_NAME', 'propai_nexus.db')

class User(UserMixin):
    def __init__(self, id, username, password_hash, role):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.role = role

    @staticmethod
    def get(user_id):
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        conn.close()
        if user:
            return User(user['id'], user['username'], user['password_hash'], user['role'])
        return None

def get_user_by_username(username):
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    conn.close()
    if user:
        return User(user['id'], user['username'], user['password_hash'], user['role'])
    return None

def get_user_by_id(user_id):
    return User.get(user_id)

def register_user(username, password, role='user'):
    hashed = generate_password_hash(password)
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    now = datetime.utcnow().isoformat()
    cur.execute("INSERT INTO users (username, password_hash, role, created_at) VALUES (?, ?, ?, ?)",
                (username, hashed, role, now))
    conn.commit()
    conn.close()
