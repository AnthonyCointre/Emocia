from extensions import db
from sqlalchemy.sql import func


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(100), nullable=False)

    last_name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(255), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    appointments = db.relationship(
        "Appointment",
        back_populates="user",
        cascade="all, delete-orphan"
    )


class Admin(db.Model):

    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(255), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    appointments = db.relationship(
        "Appointment",
        back_populates="admin",
        cascade="all, delete-orphan"
    )

    messages = db.relationship(
        "Message",
        back_populates="admin",
        cascade="all, delete-orphan"
    )


class Appointment(db.Model):

    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    admin_id = db.Column(
        db.Integer,
        db.ForeignKey("admins.id"),
        nullable=False
    )

    date = db.Column(db.String(20), nullable=False)

    time = db.Column(db.String(10), nullable=False)

    user = db.relationship(
        "User",
        back_populates="appointments"
    )

    admin = db.relationship(
        "Admin",
        back_populates="appointments"
    )


class Message(db.Model):

    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)

    admin_id = db.Column(
        db.Integer,
        db.ForeignKey("admins.id"),
        nullable=False
    )

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(255), nullable=False)

    subject = db.Column(db.String(255), nullable=False)

    message = db.Column(db.Text, nullable=False)

    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now()
    )

    admin = db.relationship(
        "Admin",
        back_populates="messages"
    )
