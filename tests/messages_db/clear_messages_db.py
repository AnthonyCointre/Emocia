from utils.db import get_db_connection

conn = get_db_connection("DATABASE_MESSAGES")
cursor = conn.cursor()

cursor.execute("DELETE FROM messages")
print(f"{cursor.rowcount} message(s) deleted.")

cursor.execute("DELETE FROM sqlite_sequence WHERE name='messages'")

conn.commit()
conn.close()

print("Messages database cleared.")
