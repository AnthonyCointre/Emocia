from app.extensions import db
from sqlalchemy.sql import func


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

    subject = db.Column(db.String(150), nullable=False)

    message = db.Column(db.String(1000), nullable=False)

    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now()
    )

    admin = db.relationship(
        "Admin",
        back_populates="messages"
    )
