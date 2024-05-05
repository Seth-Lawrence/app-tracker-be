from unittest import TestCase
from flask_bcrypt import generate_password_hash
from datetime import datetime


from app_tracker.test_config import verify_test_env_or_error
from app_tracker.app import app
from app_tracker.database import db
from app_tracker.applications.models import Application
from app_tracker.users.models import User


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

# verify that the test environ is correct
verify_test_env_or_error()


app.config['TESTING'] = True


class UsersTestCase(TestCase):
    def setUp(self):
        '''setting up data for testing'''
        self.client = app.test_client()

        db.drop_all()
        db.create_all()

        User.query.delete()

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


    def tearDown(self):
        '''clean up any fouled transactions'''

        db.session.rollback()


    def test_setup(self):
        '''test to see if tests are setup correctly'''
        test_setup_correct = True
        self.assertEqual(test_setup_correct, True)


    def test_u1_added(self):
        '''tests if first user was added correctly'''

        u1 = User.query.all()

        self.assertEqual(u1[0].username, 'test_user_1')
        self.assertEqual(u1[0].name, 'u1')
        self.assertIsNotNone(u1[0].password)


    def test_u2_added(self):
        '''tests if second user was added correctly'''

        resp = User.query.filter(User.name == 'u2')
        print(resp)
        user = resp[0]

        self.assertEqual(user.username, 'test_user_2')
        self.assertEqual(user.name, 'u2')
        self.assertIsNotNone(user.password)

        # ensuring the password is not in plain text
        self.assertNotEqual(user.password, 'password')


    def test_register_method(self):
        '''tests if register method works'''

        user_data = {
            'username': 'registered_user',
            'name': 'registered_name',
            'password': 'password'
        }

        user = User.register(user_data)
        self.assertEqual(user.username, 'registered_user')

        # ensuring the password is not in plain text
        self.assertNotEqual(user.password, 'password')
        self.assertIsNotNone(user.password)


    def test_authenticate(self):
        '''tests if authenticate works'''

        auth = User.authenticate('test_user_1', 'password1')

        self.assertTrue(auth)


    def test_invalid_authentication(self):
        '''tests to ensure invalid creds don't sign in'''

        auth = User.authenticate('test_user_1', 'invalid_password')

        self.assertFalse(auth)


    def test_adding_application(self):
        '''tests adding an application to an existing user'''
        resp = User.query.filter(User.username == 'test_user_1')

        user = resp[0]

        print(user)

        app = user.add_application(APPLICATION_DATA)

        db.session.add(app)
        db.session.commit()

        application = Application.query.all()[0].serialize()

        self.assertEqual(application['user_id'], 1)


    def test_user_application_ref(self):
        '''
        tests that using the 'application' property
        results in a list of user applications
        '''
        resp = User.query.filter(User.username == 'test_user_1')

        user = resp[0]

        print(user)

        app = user.add_application(APPLICATION_DATA)

        db.session.add(app)
        db.session.commit()

        application = user.apps[0].serialize()

        self.assertEqual(len(user.apps), 1)
        print('user applications', user.apps[0])
        self.assertIn('job_title', application)
        self.assertEqual(application['job_title'], 't_title')
