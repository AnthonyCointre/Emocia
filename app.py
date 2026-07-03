import os
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from config import Config
from extensions import db
from routes.main_routes import main_bp
from routes.booking_routes import booking_bp
from routes.auth_routes import auth_bp
from routes.admin_routes import admin_bp

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

app.config.from_object(Config)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

CORS(app, origins=[
    "http://localhost:5000",
    "https://emocia-67rj.onrender.com"
])

app.register_blueprint(main_bp)
app.register_blueprint(booking_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=True)
