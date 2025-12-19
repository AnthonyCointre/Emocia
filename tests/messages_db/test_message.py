import requests
from utils.db import get_db_connection

BASE_URL = "http://127.0.0.1:5000"
CONTACT_URL = f"{BASE_URL}/contact"

test_data = {
    "name": "Test",
    "email": "test@test.com",
    "subject": "Test",
    "message": "TEST"
}

print("=== Sending contact message ===")
response = requests.post(CONTACT_URL, json=test_data)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code, response.json())

print("\n=== Checking message in database ===")
conn = get_db_connection("DATABASE_MESSAGES")
cursor = conn.cursor()
cursor.execute(
    "SELECT * FROM messages WHERE name = ? AND email = ? AND subject = ? AND message = ?",
    (test_data['name'], test_data['email'],
     test_data['subject'], test_data['message'])
)
message = cursor.fetchone()
if message:
    print("Message exists in DB:", message)
else:
    print("No message found in DB.")

print("\n=== Cleaning up test message ===")
cursor.execute(
    "DELETE FROM messages WHERE name = ? AND email = ? AND subject = ? AND message = ?",
    (test_data['name'], test_data['email'],
     test_data['subject'], test_data['message'])
)
conn.commit()
if cursor.rowcount:
    print("Message deleted successfully.")
else:
    print("No message found to delete.")
conn.close()
