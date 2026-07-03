import re
import os
import jwt
from functools import wraps
from flask import request, redirect, url_for, session, jsonify


def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def is_strong_password(password):
    return len(password) >= 8 and re.search(r"[0-9]", password) and re.search(r"[A-Z]", password)


def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization") or session.get("jwt")
        if not token:
            if request.accept_mimetypes.accept_html:
                return redirect(url_for('auth.login'))
            return jsonify({"message": "Token missing"}), 401
        try:
            data = jwt.decode(token, os.getenv(
                "JWT_SECRET_KEY"), algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            if request.accept_mimetypes.accept_html:
                session.pop('jwt', None)
                return redirect(url_for('auth.login'))
            return jsonify({"message": "Token expired"}), 401
        except jwt.InvalidTokenError:
            if request.accept_mimetypes.accept_html:
                session.pop('jwt', None)
                return redirect(url_for('auth.login'))
            return jsonify({"message": "Invalid token"}), 401
        return f(*args, **kwargs, user_data=data)
    return decorated
