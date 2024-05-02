# from unittest import TestCase
# from flask import session, g

from app_tracker.test_config import verify_test_env_or_error
# from app_tracker.auth.models import Auth
# from app_tracker.config import USER
from app_tracker.app import app
# from app_tracker.database import db

#TODO: write tests for authentication classes

USERNAME = 'test_username'

app.config['TESTING'] = True

verify_test_env_or_error()

# class TestAuthentications(TestCase):

#     def setUp(self):
#         db.drop_all()
#         db.create_all()

#     def test_do_login(self):
#         '''tests adding username to session'''
#         with app.test_client():
#             with app.app_context():
#                 Auth.do_login(USERNAME)
#                 self.assertEquals(session[USER],USERNAME)
