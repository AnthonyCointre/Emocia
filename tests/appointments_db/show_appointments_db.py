from utils.db import get_db_connection

conn = get_db_connection("DATABASE_APPOINTMENTS")
cursor = conn.cursor()

cursor.execute(
    "SELECT id, full_name, email, date, time, status FROM appointments")
appointments = cursor.fetchall()

if appointments:
    for appt in appointments:
        print(
            f"ID: {appt[0]}, Name: {appt[1]}, Email: {appt[2]}, Date: {appt[3]}, Time: {appt[4]}, Status: {appt[5]}")
else:
    print("No appointments found.")

conn.close()
