from utils.db import get_db_connection


def get_user(email):
    conn = get_db_connection("DATABASE_USERS")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user


def get_user_admin(email):
    conn = get_db_connection("DATABASE_USERS_ADMIN")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM admins WHERE email = ?", (email,))
    admin = cursor.fetchone()
    conn.close()
    return admin


def save_user(first_name, last_name, email, hashed_password):
    conn = get_db_connection("DATABASE_USERS")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, ?, ?)",
        (first_name, last_name, email, hashed_password)
    )
    conn.commit()
    conn.close()
