import bcrypt
from utils.db import get_db_connection

email = "test@admin.com"
password = "Admin123"

hashed_password = bcrypt.hashpw(password.encode(
    'utf-8'), bcrypt.gensalt()).decode('utf-8')

conn = get_db_connection("DATABASE_USERS_ADMIN")
cursor = conn.cursor()

cursor.execute("INSERT INTO admins (email, password) VALUES (?, ?)",
               (email, hashed_password))
conn.commit()
print("Admin created successfully.")

conn.close()
