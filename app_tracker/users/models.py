from app_tracker.database import db
from flask_bcrypt import Bcrypt, generate_password_hash
from app_tracker.applications.models import Application
from datetime import datetime

bcrypt = Bcrypt()

class User(db.Model):
    '''model for user class'''

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )

    name = db.Column(
        db.String(20),
        nullable=True,
    )

    username = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(),
        nullable=False
    )

    apps = db.relationship('Application')

    @classmethod
    def register(self, username:str, name:str, password:str):

        hashed_pwd = generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            name=name,
            password=hashed_pwd,
        )
        #FIXME: returning user and adding user in the route, but will break tests

        # db.session.add(user)
        # db.session.commit()

        return user

    def add_application(self,
                        status:str,
                        company_name:str,
                        job_title:str,
                        city:str,
                        state:str,
                        cover_letter:bool,
                        remote:bool | None,
                        app_recived_confirm:bool | None,
                        farthest_round_cat: str,
                        outreach:bool | None,
                        outreach_response:bool | None,
                        referral:bool | None,
                        result_date:datetime | None,
                        min_pay:int | None = None,
                        max_pay:int | None = None,
                        outreach_date:datetime | None = datetime,
                        num_rounds_reached: int = 0
    ):
        '''adds new application for user'''

        app = Application(
            user_id = self.id,
            status = status,
            company_name = company_name,
            job_title = job_title,
            remote = remote,
            city = city,
            state = state,
            cover_letter = cover_letter,
            app_recived_confirm = app_recived_confirm,
            farthest_round_cat = farthest_round_cat,
            outreach = outreach,
            outreach_response = outreach_response,
            referral = referral,
            result_date = result_date,
            min_pay = min_pay,
            max_pay = max_pay,
            outreach_date = outreach_date,
            num_rounds_reached = num_rounds_reached
        )
        #FIXME: make sure you're adding instances in the testing & in the routes,
        # will break tests until fixed.


        # db.session.add(app)
        # db.session.commit()

        return app