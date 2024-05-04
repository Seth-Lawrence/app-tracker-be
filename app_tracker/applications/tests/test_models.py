from unittest import TestCase
from app_tracker.app import app
from app_tracker.database import db
from app_tracker.applications.models import Application
from app_tracker.test_config import verify_test_env_or_error

#verifying that env is in test
verify_test_env_or_error()

app.config['TESTING'] = True


# class TestApplications(TestCase):
#     '''testing application models'''

#     def setUp(self) -> None:
#         db.drop_all()
#         db.create_all

#     def tearDown(self) -> None:
#         return super().tearDown()

#     def test_serialize()

