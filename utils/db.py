from dotenv import load_dotenv
import os
import sqlite3

load_dotenv()


def get_db_connection(db_env_var):
    db_url = os.getenv(db_env_var)
    if db_url is None:
        raise ValueError(f"Environment variable '{db_env_var}' not set")
    if db_url.startswith("sqlite:///"):
        db_path = db_url.replace("sqlite:///", "")
        return sqlite3.connect(db_path)
    raise ValueError("Unsupported database URL")
