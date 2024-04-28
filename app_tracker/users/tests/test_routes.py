from unittest import TestCase
from flask import json

from app_tracker.app import app
from app_tracker.database import db
from app_tracker.test_config import verify_test_env_or_error
from app_tracker.users.models import User

TEST_USER_DATA = {
    'username': 'global_test_user',
    'name': 't_name',
    'password': 't_password'
}

BASE_API = '/api/user/'

# ensuring that we're in the test environment
verify_test_env_or_error()

app.config['TESTING'] = True


class UserRoutesTestCase(TestCase):
    def setUp(self):
        '''setting up for testing'''

        db.drop_all()
        db.create_all()

        user = User.register(TEST_USER_DATA)
        db.session.add(user)
        db.session.commit()

    def tearDown(self) -> None:
        '''rollback any fouled transactions'''

        db.session.rollback()

    def test_registration(self):
        '''tests to see if a user can register'''

        test_user_data = {
            'username': 'test',
            'name': 'test_name',
            'password': 'test_password'
        }

        with app.test_client() as client:
            resp = client.post(f'{BASE_API}register',
                               json=test_user_data
                               )

            user = resp.json['user']

            print('USER', user['name'])

            self.assertEqual(user['username'], 'test')
            self.assertEqual(user['name'], 'test_name')
            self.assertNotEqual(user['password'], 'test_password')

    def test_authenticate(self):
        '''tests user sign in'''

        user_signin = {
            'username': 'global_test_user',
            'password': 't_password'
        }

        with app.test_client() as client:
            resp = client.post(f'{BASE_API}signin',
                               json=user_signin)

        self.assertEqual(resp.json, True)
