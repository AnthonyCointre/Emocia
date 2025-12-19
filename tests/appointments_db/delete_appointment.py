from utils.db import get_db_connection

full_name = "Test TEST"
email = "test@test.com"
date = "2026-01-01"
time = "09:00"

conn = get_db_connection("DATABASE_APPOINTMENTS")
cursor = conn.cursor()

cursor.execute(
    "DELETE FROM appointments WHERE full_name = ? AND email = ? AND date = ? AND time = ?",
    (full_name, email, date, time)
)
conn.commit()

if cursor.rowcount:
    print("Appointment deleted successfully.")
else:
    print("No appointment found for that email and time slot.")

conn.close()
