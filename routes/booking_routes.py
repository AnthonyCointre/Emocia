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

    data = request.get_json() if request.is_json else request.form

    try:
        date = data["date"]
        time = data["time"]
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e.args[0]}"}), 400

    if not all([date, time]):
        return jsonify({"error": "All fields are required"}), 400

    conn = get_db_connection("DATABASE_URL")
    cursor = conn.cursor()

    user_id = user_data["user_id"]
    cursor.execute("""
        SELECT id FROM appointments
        WHERE date = ? AND time = ?
    """, (date, time))

    if cursor.fetchone():
        conn.close()

        msg = "This time slot is already booked. Please choose another one."

        if request.is_json:
            return jsonify({"error": msg}), 400

        flash(msg, "error")
        return redirect(url_for("booking.booking"))

    cursor.execute("""
        INSERT INTO appointments (user_id, date, time)
        VALUES (?, ?, ?)
    """, (user_id, date, time))

    conn.commit()
    conn.close()

    if request.is_json:
        return jsonify({"success": "Appointment booked successfully"}), 200

    return redirect(url_for('booking.booking_success'))


@booking_bp.route('/booking/success')
def booking_success():
    return render_template("booking_success.html")
