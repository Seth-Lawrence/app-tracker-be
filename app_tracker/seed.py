from app_tracker.app import app
from app_tracker.users.models import User
from app_tracker.database import db
# from app_tracker.applications.models import Application

with app.app_context():
    db.drop_all()
    db.create_all()

user_data = {
    'username': 'u1',
    'name': 'user_1',
    'password': 'password1'
}

User.register(user_data)
