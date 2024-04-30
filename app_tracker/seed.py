from app_tracker.app import app
from app_tracker.users.models import User
from app_tracker.database import db

with app.app_context():
    db.drop_all()
    db.create_all()

user_data = {
    'username': 'u1',
    'name': 'user_1',
    'password': 'password1'
}

user = User.register(user_data)
db.session.add(user)
db.session.commit()
