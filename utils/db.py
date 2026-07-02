import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()


def get_db_connection(db_env_var="DATABASE_URL"):
    db_url = os.getenv(db_env_var)

    if not db_url:
        raise ValueError(f"Environment variable '{db_env_var}' not set")

    if db_url.startswith("sqlite:///"):
        db_path = db_url.replace("sqlite:///", "")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    raise ValueError("Unsupported database URL")
