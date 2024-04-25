from unittest import TestCase

from app_tracker.app import app
from app_tracker.database import db
from app_tracker.test_config import verify_test_env_or_error
from app_tracker.users.models import User

# ensuring that we're in the test environment
verify_test_env_or_error()

app.config['TESTING'] = True

db.drop_all()
db.create_all()


class UserRoutesTestCase(TestCase):
    '''tests user routes'''

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

            print('RESPONSE', resp)

            self.assertEqual(resp.username, 'test')
            self.assertequal(resp.name, 'test_name')
            self.assertNotEqual(resp.password, 'test_password')
