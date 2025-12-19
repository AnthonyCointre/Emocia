from utils.db import get_db_connection

conn = get_db_connection("DATABASE_APPOINTMENTS")
cursor = conn.cursor()

cursor.execute("""
SELECT name FROM sqlite_master WHERE type='table' AND name='appointments';
""")

if cursor.fetchone():
    print("appointments.db already exists.")
else:
    cursor.execute("""
        CREATE TABLE appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            status TEXT DEFAULT 'pending'
        );
    """)

    cursor.execute("""
        CREATE TABLE availability (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL
        );
    """)

    conn.commit()
    print("appointments.db created successfully.")

conn.close()
