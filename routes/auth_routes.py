import os
import datetime
import bcrypt
import jwt
from flask import Blueprint, request, redirect, url_for, session, render_template
from controllers.user_controllers import get_user, save_user, get_user_admin
from utils.helpers import is_valid_email, is_strong_password, jwt_required
from utils.db import get_db_connection

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        action = request.form.get('action')
        email = request.form['email']
        password = request.form['password']

        if action == 'login':
            admin = get_user_admin(email)
            if admin and bcrypt.checkpw(password.encode('utf-8'), admin[2].encode('utf-8')):
                session['admin'] = email
                payload = {"user_id": admin[0], "email": admin[1], "role": "admin",
                           "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
                token = jwt.encode(payload, os.getenv(
                    "JWT_SECRET_KEY"), algorithm="HS256")
                session['jwt'] = token
                return redirect(url_for('main.home'))

            user = get_user(email)
            if user and bcrypt.checkpw(password.encode('utf-8'), user[4].encode('utf-8')):
                session['email'] = email
                payload = {"user_id": user[0], "email": user[3], "role": "user",
                           "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
                token = jwt.encode(payload, os.getenv(
                    "JWT_SECRET_KEY"), algorithm="HS256")
                session['jwt'] = token
                return redirect(url_for('main.home'))

            return render_template('login.html', error='Invalid email or password.')

        elif action == 'sign-up':
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            if not is_valid_email(email):
                return render_template('login.html', error='Invalid email format.')
            if not is_strong_password(password):
                return render_template('login.html', error='Password must be at least 8 characters, include a number and an uppercase letter.')
            if get_user(email):
                return render_template('login.html', error='Email already registered.')

            hashed_password = bcrypt.hashpw(password.encode(
                'utf-8'), bcrypt.gensalt()).decode('utf-8')
            save_user(first_name, last_name, email, hashed_password)

            session['email'] = email
            user = get_user(email)
            payload = {"user_id": user[0], "email": user[3], "role": "user",
                       "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
            token = jwt.encode(payload, os.getenv(
                "JWT_SECRET_KEY"), algorithm="HS256")
            session['jwt'] = token
            return redirect(url_for('main.home'))

    return render_template('login.html')


@auth_bp.route('/account', methods=['GET', 'POST'])
@jwt_required
def account(user_data):
    email = user_data['email']
    print("EMAIL FROM JWT:", email)
    user = get_user(email)
    print("USER FROM DB:", user)
    conn = get_db_connection("DATABASE_APPOINTMENTS")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT date, time, full_name FROM appointments WHERE email = ? ORDER BY date, time", (email,))
    appointments = cursor.fetchall()
    conn.close()

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'delete':
            conn_appt = get_db_connection("DATABASE_APPOINTMENTS")
            cursor_appt = conn_appt.cursor()
            cursor_appt.execute(
                "DELETE FROM appointments WHERE email = ?", (email,))
            conn_appt.commit()
            conn_appt.close()

            conn_user = get_db_connection("DATABASE_USERS")
            cursor_user = conn_user.cursor()
            cursor_user.execute("DELETE FROM users WHERE email = ?", (email,))
            conn_user.commit()
            conn_user.close()

            session.pop('email', None)
            session.pop('jwt', None)
            return redirect(url_for('main.home'))

    return render_template('account.html', user=user, appointments=appointments)


@auth_bp.route('/logout')
@jwt_required
def logout(user_data):
    session.pop('email', None)
    session.pop('jwt', None)
    return redirect(url_for('main.home'))
