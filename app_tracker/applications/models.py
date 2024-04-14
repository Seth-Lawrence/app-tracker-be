from app_tracker.database import db


class Application(db.Model):

    __tablename__ = 'applications'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )

    company_name = db.Column(
        db.String(50),
        nullable=False,
    )

    job_title = db.Column(
        db.String(50)

    )