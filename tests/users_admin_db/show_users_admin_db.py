from utils.db import get_db_connection

conn = get_db_connection("DATABASE_USERS_ADMIN")
cursor = conn.cursor()

cursor.execute("SELECT id, email FROM admins")
admins = cursor.fetchall()

if admins:
    for admin in admins:
        print(f"ID: {admin[0]}, Email: {admin[1]}")
else:
    print("No admins found.")

conn.close()
