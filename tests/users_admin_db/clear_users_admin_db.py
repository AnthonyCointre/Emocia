from utils.db import get_db_connection

conn = get_db_connection("DATABASE_USERS_ADMIN")
cursor = conn.cursor()

cursor.execute("DELETE FROM admins WHERE email != 'admin@admin.com'")
print(f"{cursor.rowcount} admin(s) deleted (default admin preserved).")

cursor.execute("DELETE FROM sqlite_sequence WHERE name='admins'")

conn.commit()
conn.close()

print("Admin database cleared (default admin preserved).")
