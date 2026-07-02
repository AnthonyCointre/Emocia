from flask import Blueprint, render_template, request, redirect, url_for, session
from routes.auth_routes import jwt_required
from utils.db import get_db_connection

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/account')
@jwt_required
def admin_account(user_data):

    conn = get_db_connection("DATABASE_URL")
    cursor = conn.cursor()

    # APPOINTMENTS (relationnel)
    cursor.execute("""
        SELECT
            a.id,
            u.first_name,
            u.last_name,
            u.email,
            a.date,
            a.time
        FROM appointments a
        JOIN users u ON a.user_id = u.id
        ORDER BY a.date, a.time
    """)
    all_appointments = cursor.fetchall()

    # MESSAGES
    cursor.execute("""
        SELECT id, name, email, subject, message, created_at
        FROM messages
        ORDER BY created_at DESC
    """)
    messages = cursor.fetchall()

    conn.close()

    return render_template(
        'admin_account.html',
        appointments=all_appointments,
        messages=messages
    )


@admin_bp.route('/appointment/delete', methods=['POST'])
@jwt_required
def delete_appointment(user_data):

    appointment_id = request.form.get('appointment_id')
    if not appointment_id:
        return "Invalid input", 400

    conn = get_db_connection("DATABASE_URL")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM appointments WHERE id = ?",
        (appointment_id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for('admin.admin_account'))


@admin_bp.route('/message/delete', methods=['POST'])
@jwt_required
def delete_message(user_data):

    message_id = request.form.get('message_id')
    if not message_id:
        return "Invalid input", 400

    conn = get_db_connection("DATABASE_URL")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM messages WHERE id = ?",
        (message_id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for('admin.admin_account'))


@admin_bp.route('/logout')
@jwt_required
def admin_logout(user_data):
    session.pop('admin', None)
    session.pop('jwt', None)
    return redirect(url_for('main.home'))
