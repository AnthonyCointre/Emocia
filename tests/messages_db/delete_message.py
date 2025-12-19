from utils.db import get_db_connection

name = "Test TEST"
email = "test@test.com"
subject = "Test"
message = "TEST"

conn = get_db_connection("DATABASE_MESSAGES")
cursor = conn.cursor()

cursor.execute(
    "DELETE FROM messages WHERE name = ? AND email = ? AND subject = ? AND message = ?",
    (name, email, subject, message)
)
conn.commit()

if cursor.rowcount:
    print("Message deleted successfully.")
else:
    print("No message found for that email and subject.")

conn.close()
