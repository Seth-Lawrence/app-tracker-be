from unittest import TestCase
from flask_bcrypt import generate_password_hash

from app_tracker.app import app
from app_tracker.database import db
from app_tracker.test_config import verify_test_env_or_error
from app_tracker.users.models import User
from app_tracker.applications.models import Application


app.config['TESTING'] = True

#ensuring that we're in the test db
verify_test_env_or_error()

BASE_API =  '/api/application/'

APPLICATION_DATA = {
    'status': 'active',
    'company_name': 'test_company',
    'job_title': 't_title',
    'remote': True,
    'city': 't_city',
    'state': 't_state',
    'cover_letter': True,
    'app_received_confirm': True,
    'farthest_round_cat': 'application',
    'outreach': True,
    'outreach_response': True,
    'referral': True,
    'result_date': None,
    'min_pay': None,
    'max_pay': None,
    'outreach_date': None,
    'num_rounds_reached': None
}

U1_SIGNIN = {
    'username': 'test_user_1',
    'password': 'password1'
}

class TestApplicationRoutes(TestCase):
    '''testing if the application routes work'''

    def setUp(self) -> None:
        db.drop_all()
        db.create_all()

        self.u1 = User(
            name='u1',
            username='test_user_1',
            password=generate_password_hash('password1').decode('utf-8')
        )

        self.u2 = User(
            name='u2',
            username='test_user_2',
            password=generate_password_hash('password2').decode('utf-8')
        )

        db.session.add(self.u1)
        db.session.add(self.u2)
        db.session.commit()

        application = self.u1.add_application(APPLICATION_DATA)

        db.session.add(application)
        db.session.commit()

    def tearDown(self) -> None:
        '''clear any fouled transactions'''

        db.session.rollback()

    def test_get_applications(self):
        '''tests to to ensure get application route works'''

        with app.test_client() as client:
            with app.app_context():
                client.post('/api/user/login',
                            json = U1_SIGNIN)

        with app.test_client() as client:
            resp = app.get(f'{BASE_API}all')

            print('RESPONSE', resp)

            self.assertEqual(len(resp),1)