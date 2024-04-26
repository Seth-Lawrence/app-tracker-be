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

# ensuring that we're in the test environment
verify_test_env_or_error()

app.config['TESTING'] = True

db.drop_all()
db.create_all()


class UserRoutesTestCase(TestCase):
    def setUp(self):
        '''setting up for testing'''
        User.register(TEST_USER_DATA)



    def test_registration(self):
        '''tests to see if a user can register'''

        test_user_data = {
            'username': 'test',
            'name': 'test_name',
            'password': 'test_password'
        }

        with app.test_client() as client:
            resp = client.post('/api/user/register',
                               json=test_user_data
                            )

            user = resp.json['user']

            print('USER', user['name'])

            self.assertEqual(user['username'], 'test')
            self.assertEqual(user['name'], 'test_name')
            self.assertNotEqual(user['password'], 'test_password')

    def test_authenticate():
        '''tests user sign in'''
        ...




