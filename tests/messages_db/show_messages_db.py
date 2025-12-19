from utils.db import get_db_connection

conn = get_db_connection("DATABASE_MESSAGES")
cursor = conn.cursor()

cursor.execute(
    "SELECT id, name, email, subject, message, created_at FROM messages")
messages = cursor.fetchall()

if messages:
    for msg in messages:
        print(
            f"ID: {msg[0]}, Name: {msg[1]}, Email: {msg[2]}, Subject: {msg[3]}, Message: {msg[4]}, Received At: {msg[5]}")
else:
    print("No messages found.")

conn.close()
