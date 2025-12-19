from utils.db import get_db_connection

email = "test@admin.com"

conn = get_db_connection("DATABASE_USERS_ADMIN")
cursor = conn.cursor()

cursor.execute("DELETE FROM admins WHERE email = ?", (email,))
conn.commit()

if cursor.rowcount:
    print("Admin deleted successfully.")
else:
    print("No admin found with that email.")

conn.close()
