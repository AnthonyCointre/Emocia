import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

db_url = os.getenv("DATABASE_URL")

if db_url.startswith("sqlite:///"):
    db_path = BASE_DIR / db_url.replace("sqlite:///", "")
    db_url = f"sqlite:///{db_path}"


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
