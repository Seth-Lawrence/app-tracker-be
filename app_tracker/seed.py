from app_tracker.app import app
from app_tracker.users.models import User
from app_tracker.database import db

with app.app_context():
    db.drop_all()
    db.create_all()

User.register('test_user','test','password')
