from utils.db import get_db_connection

conn = get_db_connection("DATABASE_APPOINTMENTS")
cursor = conn.cursor()

cursor.execute("DELETE FROM appointments")
print(f"{cursor.rowcount} appointment(s) deleted.")

cursor.execute("DELETE FROM sqlite_sequence WHERE name='appointments'")

conn.commit()
conn.close()

print("Appointments database cleared.")
