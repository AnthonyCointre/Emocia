from flask import Blueprint, render_template, request, redirect, url_for, session
from routes.auth_routes import jwt_required
from utils.db import get_db_connection

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/account')
@jwt_required
def admin_account(user_data):
    conn = get_db_connection("DATABASE_APPOINTMENTS")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT full_name, email, date, time FROM appointments ORDER BY date, time")
    all_appointments = cursor.fetchall()
    conn.close()

    conn = get_db_connection("DATABASE_MESSAGES")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, email, subject, message, created_at FROM messages ORDER BY created_at DESC")
    messages = cursor.fetchall()
    conn.close()

    return render_template('admin_account.html', appointments=all_appointments, messages=messages)


@admin_bp.route('/appointment/delete', methods=['POST'])
@jwt_required
def delete_appointment(user_data):
    full_name = request.form.get('full_name')
    email = request.form.get('email')
    date = request.form.get('date')
    time = request.form.get('time')
    if not all([full_name, email, date, time]):
        return "Invalid input", 400
    conn = get_db_connection("DATABASE_APPOINTMENTS")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM appointments WHERE full_name=? AND email=? AND date=? AND time=?",
                   (full_name, email, date, time))
    conn.commit()
    conn.close()
    return redirect(url_for('admin.admin_account'))


@admin_bp.route('/message/delete', methods=['POST'])
@jwt_required
def delete_message(user_data):
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    created_at = request.form.get('created_at')
    if not all([name, email, subject, created_at]):
        return "Invalid input", 400
    conn = get_db_connection("DATABASE_MESSAGES")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM messages WHERE name=? AND email=? AND subject=? AND created_at=?",
                   (name, email, subject, created_at))
    conn.commit()
    conn.close()
    return redirect(url_for('admin.admin_account'))


@admin_bp.route('/logout')
@jwt_required
def admin_logout(user_data):
    session.pop('admin', None)
    session.pop('jwt', None)
    return redirect(url_for('main.home'))
