from utils.db import get_db_connection

conn = get_db_connection("DATABASE_MESSAGES")
cursor = conn.cursor()

cursor.execute("""
SELECT name FROM sqlite_master WHERE type='table' AND name='messages';
""")

if cursor.fetchone():
    print("messages.db already exists.")
else:
    cursor.execute("""
        CREATE TABLE messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            subject TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    print("messages.db created successfully.")

conn.close()
