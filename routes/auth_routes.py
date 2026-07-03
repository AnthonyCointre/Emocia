import os
import datetime
import bcrypt
import jwt
from flask import Blueprint, request, redirect, url_for, session, render_template
from models import User, Admin, Appointment
from extensions import db
from utils.helpers import is_valid_email, is_strong_password, jwt_required


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        action = request.form.get('action')
        email = request.form['email']
        password = request.form['password']

        if action == 'login':

            admin = Admin.query.filter_by(email=email).first()

            if admin and bcrypt.checkpw(
                password.encode('utf-8'),
                admin.password.encode('utf-8')
            ):
                session['admin'] = admin.email

                payload = {
                    "user_id": admin.id,
                    "email": admin.email,
                    "role": "admin",
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
                }

                token = jwt.encode(
                    payload,
                    os.getenv("JWT_SECRET_KEY"),
                    algorithm="HS256"
                )

                session['jwt'] = token

                return redirect(url_for('main.home'))

            user = User.query.filter_by(email=email).first()

            if user and bcrypt.checkpw(
                password.encode('utf-8'),
                user.password.encode('utf-8')
            ):
                session['user'] = user.email

                payload = {
                    "user_id": user.id,
                    "email": user.email,
                    "role": "user",
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
                }

                token = jwt.encode(
                    payload,
                    os.getenv("JWT_SECRET_KEY"),
                    algorithm="HS256"
                )

                session['jwt'] = token

                return redirect(url_for('main.home'))

            return render_template('login.html', error='Invalid email or password.')

        elif action == 'sign-up':

            first_name = request.form['first_name']
            last_name = request.form['last_name']

            if not is_valid_email(email):
                return render_template('login.html', error='Invalid email format.')

            if not is_strong_password(password):
                return render_template(
                    'login.html',
                    error='Password must be at least 8 characters, include a number and an uppercase letter.'
                )

            if User.query.filter_by(email=email).first():
                return render_template('login.html', error='Email already registered.')

            hashed_password = bcrypt.hashpw(
                password.encode('utf-8'),
                bcrypt.gensalt()
            ).decode('utf-8')

            user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=hashed_password
            )

            db.session.add(user)
            db.session.commit()

            session['user'] = user.email

            payload = {
                "user_id": user.id,
                "email": user.email,
                "role": "user",
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }

            token = jwt.encode(
                payload,
                os.getenv("JWT_SECRET_KEY"),
                algorithm="HS256"
            )

            session['jwt'] = token

            return redirect(url_for('main.home'))

    return render_template('login.html')


@auth_bp.route('/account', methods=['GET', 'POST'])
@jwt_required
def account(user_data):

    user = User.query.get(user_data["user_id"])

    appointments = (
        Appointment.query
        .filter_by(user_id=user.id)
        .order_by(Appointment.date, Appointment.time)
        .all()
    )

    if request.method == 'POST':

        action = request.form.get('action')

        if action == 'delete':

            db.session.delete(user)
            db.session.commit()

            session.pop('user', None)
            session.pop('jwt', None)

            return redirect(url_for('main.home'))

    return render_template(
        'account.html',
        user=user,
        appointments=appointments
    )


@auth_bp.route('/logout')
@jwt_required
def logout(user_data):

    session.pop('user', None)
    session.pop('jwt', None)

    return redirect(url_for('main.home'))
