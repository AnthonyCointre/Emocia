from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from utils.db import get_db_connection

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/home')
def home():
    return render_template('home.html')


@main_bp.route('/about')
def about():
    return render_template('about.html')


@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            try:
                name = data['name']
                email = data['email']
                subject = data['subject']
                message = data['message']
            except KeyError as e:
                return jsonify({"error": f"Missing field: {e.args[0]}"}), 400
        else:
            try:
                name = request.form['name']
                email = request.form['email']
                subject = request.form['subject']
                message = request.form['message']
            except KeyError as e:
                return jsonify({"error": f"Missing field: {e.args[0]}"}), 400

        if not all([name, email, subject, message]):
            return jsonify({"error": "All fields are required"}), 400

        conn = get_db_connection("DATABASE_MESSAGES")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                subject TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        cursor.execute(
            "INSERT INTO messages (name, email, subject, message) VALUES (?, ?, ?, ?)",
            (name, email, subject, message)
        )
        conn.commit()
        conn.close()

        if request.is_json:
            return jsonify({"success": "Message received"}), 200
        else:
            return redirect(url_for('main.contact'))

    return render_template('contact.html')
