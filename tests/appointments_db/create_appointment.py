from utils.db import get_db_connection

full_name = "Test TEST"
email = "test@test.com"
date = "2026-01-01"
time = "09:00"

conn = get_db_connection("DATABASE_APPOINTMENTS")
cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM appointments WHERE date = ? AND time = ?", (date, time))
if cursor.fetchone():
    print(f"Error: The slot on {date} at {time} is already booked.")
else:
    cursor.execute(
        "INSERT INTO appointments (full_name, email, date, time) VALUES (?, ?, ?, ?)",
        (full_name, email, date, time)
    )
    conn.commit()
    print("Appointment created successfully.")

conn.close()
