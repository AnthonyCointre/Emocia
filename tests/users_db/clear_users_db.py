from utils.db import get_db_connection

conn = get_db_connection("DATABASE_USERS")
cursor = conn.cursor()

cursor.execute("DELETE FROM users")
print(f"{cursor.rowcount} user(s) deleted.")

cursor.execute("DELETE FROM sqlite_sequence WHERE name='users'")

conn.commit()
conn.close()

print("Users database cleared.")
