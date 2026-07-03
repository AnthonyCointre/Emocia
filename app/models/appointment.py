from app.extensions import db


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
