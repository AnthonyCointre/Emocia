from app.extensions import db


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
