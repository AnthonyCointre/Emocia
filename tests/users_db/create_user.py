import bcrypt
from utils.db import get_db_connection

first_name = "Test"
last_name = "TEST"
email = "test@test.com"
password = "Test123"

hashed_password = bcrypt.hashpw(password.encode(
    'utf-8'), bcrypt.gensalt()).decode('utf-8')

conn = get_db_connection("DATABASE_USERS")
cursor = conn.cursor()

cursor.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, ?, ?)",
               (first_name, last_name, email, hashed_password))
conn.commit()
print("User created successfully.")

conn.close()
