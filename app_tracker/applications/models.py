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
        db.String(),
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

    notes = db.Column(
        db.String()
    )

    job_link = db.Column(
        db.String()
    )

    def serialize(self):
        '''serialize to dictionary'''

        return {
           'user_id': self.user_id,
           'status': self.status,
           'company_name': self.company_name,
           'job_title': self.job_title,
           'remote': self.remote,
           'city': self.city,
           'state': self.state,
           'min_pay': self.min_pay,
           'max_pay': self.max_pay,
           'cover_letter': self.cover_letter,
           'app_received_confirm': self.app_received_confirm,
           'num_rounds_reached': self.num_rounds_reached,
           'farthest_round_cat': self.farthest_round_cat,
           'outreach': self.outreach,
           'outreach_date': self.outreach_date,
           'outreach_response': self.outreach_response,
           'referral': self.referral,
           'result_date': self.result_date,
           'notes': self.notes,
           'job_link': self.job_link
        }
