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

    status = db.Column(
        db.String(20)
    )

    company_name = db.Column(
        db.String(50),
        nullable=False,
    )

    job_title = db.Column(
        db.String(50),
        nullable=False
    )

    remote = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    city = db.Column(
        db.String(50),
        nullable=True
    )

    state = db.Column(
        db.String(2),
        nullable=True
    )

    min_pay = db.Column(
        db.Integer
    )

    max_pay = db.Column(
        db.Integer
    )

    cover_letter = db.Column(
        db.Boolean,
        nullable=False
    )

    app_received_confirm = db.Column(
        db.Boolean
    )

    num_rounds_reached = db.Column(
        db.Integer
    )

    farthest_round_cat = db.Column(
        db.String(40)
    )

    outreach = db.Column(
        db.Boolean
    )

    outreach_date = db.Column(
        db.DateTime,
    )

    outreach_response = db.Column(
        db.Boolean
    )

    referral = db.Column(
        db.Boolean
    )

    result_date = db.Column(
        db.DateTime
    )
