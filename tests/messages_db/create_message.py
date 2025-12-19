from utils.db import get_db_connection

name = "Test TEST"
email = "test@test.com"
subject = "Test"
message = "TEST"

conn = get_db_connection("DATABASE_MESSAGES")
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO messages (name, email, subject, message) VALUES (?, ?, ?, ?)",
    (name, email, subject, message)
)
conn.commit()
print("Message created successfully.")

conn.close()
