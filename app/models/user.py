from app.extensions import db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(50), nullable=False)

    last_name = db.Column(db.String(50), nullable=False)

    email = db.Column(db.String(255), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    appointments = db.relationship(
        "Appointment",
        back_populates="user",
        cascade="all, delete-orphan"
    )
