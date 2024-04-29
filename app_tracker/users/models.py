from app_tracker.database import db
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash
from app_tracker.applications.models import Application

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
        db.Text(),
        nullable=False
    )

    apps = db.relationship('Application')

    # TODO: test validate signup

    @classmethod
    def validate_signup(cls, user_data):
        '''validates that the signup information is valid,
        return error obj if errors, or None if validated
        '''
        errors = {}

        username = user_data.get('username', None)
        name = user_data.get('name', None)
        password = user_data.get('password', None)

        username_length = len(username)
        name_length = len(name)
        password_length = len(password)

        if username_length > 20 or username_length < 2 or not username:
            errors['username'] = (
                'username is less than 2 or greater than 20 chars'
            )
        if name_length > 20 or name_length < 2 or not name:
            errors['name'] = (
                'username is less than 2 or greater than 20 chars'
            )
        if password_length < 9 or not password:
            errors['password'] = (
                'password must be at least 9 characters'
            )

        return errors if errors else None

    @classmethod
    def register(cls, user_data):

        username = user_data['username']
        name = user_data['name']
        password = user_data['password']

        hashed_pwd = generate_password_hash(password).decode('utf-8')

        user = User(
            username=username,
            name=name,
            password=hashed_pwd,
        )

        return user

    @classmethod
    def authenticate(cls, username: str, password: str) -> bool:
        '''checks username and password and logs in user or returns none'''

        user = User.query.filter(User.username == username).one_or_none()

        if user and check_password_hash(user.password, password):
            return True

        return False

    def add_application(self, application_data: object) -> Application:
        '''adds new application for user instance'''

        app = Application(
            user_id=self.id,
            status=application_data['status'],
            company_name=application_data['company_name'],
            job_title=application_data['job_title'],
            remote=application_data['remote'],
            city=application_data['city'],
            state=application_data['state'],
            cover_letter=application_data['cover_letter'],
            app_recived_confirm=application_data['app_recived_confirm'],
            farthest_round_cat=application_data['farthest_round_cat'],
            outreach=application_data['outreach'],
            outreach_response=application_data['outreach_response'],
            referral=application_data['referral'],
            result_date=application_data['result_date'],
            min_pay=application_data['min_pay'],
            max_pay=application_data['max_pay'],
            outreach_date=application_data['outreach_date'],
            num_rounds_reached=application_data['num_rounds_reached']
        )

        return app

    def get_applications(self):
        '''gets list of applications'''

        return self.apps

    def serialize(self):
        '''serialize to dictionary'''

        return {
            'username': self.username,
            'name': self.name,
            'hashed_password': self.password
        }
