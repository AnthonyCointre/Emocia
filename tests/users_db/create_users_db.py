from utils.db import get_db_connection

conn = get_db_connection("DATABASE_USERS")
cursor = conn.cursor()

cursor.execute("""
SELECT name FROM sqlite_master WHERE type='table' AND name='users';
""")

if cursor.fetchone():
    print("users.db already exists.")
else:
    cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    print("users.db created successfully.")

conn.close()
