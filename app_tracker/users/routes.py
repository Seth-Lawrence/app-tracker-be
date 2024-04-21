from flask import Blueprint, jsonify, request
from app_tracker.database import db
from app_tracker.users.models import User

user = Blueprint('user',__name__)

@user.post('/register')
def register_user():
    '''calls register user on the api and registers the user'''

    user_data = request.json

    errors = User.validate_signup(user_data)

    if errors:
        return errors

    user = User.register(user_data)

    db.session.add(user)

    try:
        db.session.commit()
    except:
        raise RuntimeError('sign up failed')

    return user
