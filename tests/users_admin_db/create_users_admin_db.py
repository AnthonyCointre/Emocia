import bcrypt
from utils.db import get_db_connection

conn = get_db_connection("DATABASE_USERS_ADMIN")
cursor = conn.cursor()

cursor.execute("""
SELECT name FROM sqlite_master WHERE type='table' AND name='admins';
""")

if cursor.fetchone():
    print("users_admin.db already exists.")
else:
    cursor.execute("""
    CREATE TABLE admins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)
    conn.commit()

    default_email = "admin@admin.com"
    default_password = bcrypt.hashpw("Admin123".encode(
        "utf-8"), bcrypt.gensalt()).decode("utf-8")

    cursor.execute("INSERT INTO admins (email, password) VALUES (?, ?)",
                   (default_email, default_password))
    conn.commit()

    print("users_admin.db created successfully with default admin account.")

conn.close()
