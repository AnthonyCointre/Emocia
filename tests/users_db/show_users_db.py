from utils.db import get_db_connection

conn = get_db_connection("DATABASE_USERS")
cursor = conn.cursor()

cursor.execute("SELECT id, first_name, last_name, email FROM users")
users = cursor.fetchall()

if users:
    for user in users:
        print(
            f"ID: {user[0]}, First Name: {user[1]}, Last Name: {user[2]}, Email: {user[3]}")
else:
    print("No users found.")

conn.close()
