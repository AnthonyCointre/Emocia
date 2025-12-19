import requests
from utils.db import get_db_connection

BASE_URL = "http://127.0.0.1:5000"
BOOKING_URL = f"{BASE_URL}/booking/submit"

test_data = {
    "full_name": "Test TEST",
    "email": "test@test.com",
    "date": "2026-01-01",
    "time": "09:00"
}

print("=== Creating appointment ===")
response = requests.post(BOOKING_URL, json=test_data)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code, response.json())

print("\n=== Checking appointment in database ===")
conn = get_db_connection("DATABASE_APPOINTMENTS")
cursor = conn.cursor()
cursor.execute(
    "SELECT * FROM appointments WHERE full_name = ? AND email = ? AND date = ? AND time = ?",
    (test_data['full_name'], test_data['email'],
     test_data['date'], test_data['time'])
)
appointment = cursor.fetchone()
if appointment:
    print("Appointment exists in DB:", appointment)
else:
    print("No appointment found in DB.")

print("\n=== Cleaning up test appointment ===")
cursor.execute(
    "DELETE FROM appointments WHERE full_name = ? AND email = ? AND date = ? AND time = ?",
    (test_data['full_name'], test_data['email'],
     test_data['date'], test_data['time'])
)
conn.commit()
if cursor.rowcount:
    print("Appointment deleted successfully.")
else:
    print("No appointment found to delete.")
conn.close()
