from unittest import TestCase

from app_tracker.test_config import verify_test_env_or_error
from app_tracker.app import app
from app_tracker.database import db

from app_tracker.users.models import User

# verify that the test environ is correct
verify_test_env_or_error()


app.config['TESTING'] = True

db.drop_all()
db.create_all()

class UsersTestCase(TestCase):
    def setUp(self):
        '''setting up data for testing'''
        self.client = app.test_client()

        User.query.delete()

        self.u1 = User(
            name='u1',
            username='test_user_1',
            password='password'
        )

        self.u2 = User(
            name='u2',
            username='test_user_2',
            password='password2'
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

        users = User.query.all()

        self.assertEqual(users[1].username, 'test_user_2')
        self.assertEqual(users[1].name, 'u2')
        self.assertIsNotNone(users[1].password)

    def test_register_method(self):
        '''tests if register method workds'''

        User.register('registered_user','registered_name','password')
        resp = User.query.filter(User.username == 'registered_user')
        user = resp[0]

        self.assertEqual(user.username, 'registered_user')
        self.assertNotEqual(user.password, 'password')
        self.assertIsNotNone(user.password)


