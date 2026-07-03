from flask import Blueprint, render_template, request, redirect, url_for, session
from models import Appointment, Message
from extensions import db
from routes.auth_routes import jwt_required


admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/account')
@jwt_required
def admin_account(user_data):

    all_appointments = (
        Appointment.query
        .order_by(Appointment.date, Appointment.time)
        .all()
    )

    messages = (
        Message.query
        .order_by(Message.created_at.desc())
        .all()
    )

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

    appointment = Appointment.query.get(appointment_id)

    if appointment:
        db.session.delete(appointment)
        db.session.commit()

    return redirect(url_for('admin.admin_account'))


@admin_bp.route('/message/delete', methods=['POST'])
@jwt_required
def delete_message(user_data):

    message_id = request.form.get('message_id')

    if not message_id:
        return "Invalid input", 400

    message = Message.query.get(message_id)

    if message:
        db.session.delete(message)
        db.session.commit()

    return redirect(url_for('admin.admin_account'))


@admin_bp.route('/logout')
@jwt_required
def admin_logout(user_data):

    session.pop('admin', None)
    session.pop('jwt', None)

    return redirect(url_for('main.home'))
