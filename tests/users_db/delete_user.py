from utils.db import get_db_connection

email = "test@test.com"

conn = get_db_connection("DATABASE_USERS")
cursor = conn.cursor()

cursor.execute("DELETE FROM users WHERE email = ?", (email,))
conn.commit()

if cursor.rowcount:
    print("User deleted successfully.")
else:
    print("No user found with that email.")

conn.close()
