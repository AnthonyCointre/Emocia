from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from routes.auth_routes import jwt_required
from utils.db import get_db_connection

booking_bp = Blueprint('booking', __name__)


@booking_bp.route('/booking')
def booking():
    hours = [
        "09:00", "10:00", "11:00",
        "14:00", "15:00", "16:00"
    ]
    return render_template("booking.html", hours=hours)


@booking_bp.route('/booking/submit', methods=['POST'])
@jwt_required
def booking_submit(user_data):
    if request.is_json:
        try:
            data = request.get_json()
            full_name = data['full_name']
            email = data['email']
            date = data['date']
            time = data['time']
        except KeyError as e:
            return jsonify({"error": f"Missing field: {e.args[0]}"}), 400
    else:
        try:
            full_name = request.form['full_name']
            email = request.form['email']
            date = request.form['date']
            time = request.form['time']
        except KeyError as e:
            return jsonify({"error": f"Missing field: {e.args[0]}"}), 400

    if not all([full_name, email, date, time]):
        return jsonify({"error": "All fields are required"}), 400

    conn = get_db_connection("DATABASE_APPOINTMENTS")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute(
        "SELECT * FROM appointments WHERE date = ? AND time = ?", (date, time)
    )
    existing = cursor.fetchone()

    if existing:
        conn.close()
        if request.is_json:
            return jsonify({"error": "This time slot is already booked. Please choose another one."}), 400
        else:
            flash("This time slot is already booked. Please choose another one.", "error")
            return redirect(url_for('booking.booking'))

    cursor.execute(
        "INSERT INTO appointments (full_name, email, date, time) VALUES (?, ?, ?, ?)",
        (full_name, email, date, time)
    )
    conn.commit()
    conn.close()

    if request.is_json:
        return jsonify({"success": "Appointment booked successfully"}), 200
    else:
        return redirect(url_for('booking.booking_success'))


@booking_bp.route('/booking/success')
def booking_success():
    return render_template("booking_success.html")
