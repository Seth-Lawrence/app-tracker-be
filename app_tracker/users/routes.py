from flask import Blueprint, jsonify, request
from app_tracker.database import db
from app_tracker.users.models import User
from sqlalchemy import exc


user = Blueprint('user',__name__)

@user.post('/register')
def register_user():
    '''calls register user on the api and registers the user'''

    user_data = request.json

    errors = User.validate_signup(user_data)

    if errors:
        return jsonify(errors=errors)

    user = User.register(user_data)

    try:
        db.session.add(user)
        db.session.commit()
    except exc.IntegrityError:
        return jsonify(error='signup failed')

    return jsonify(user=user)
