from flask import Blueprint, jsonify, request, session
from app_tracker.database import db
from app_tracker.users.models import User
from sqlalchemy import exc


user = Blueprint('user', __name__)


@user.post('/register')
def register_user():
    '''calls register user on the api and registers the user'''

    user_data = request.json

    errors = User.validate_signup(user_data)

    if errors:
        return jsonify(errors=errors)

    user = User.register(user_data)

    db.session.add(user)

    try:
        db.session.commit()
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            error='Your username did not meet requirements. Try another.'
        )

    serialized_user = user.serialize()

    return jsonify(user=serialized_user)


@user.post('/signin')
def sign_in():
    '''signs in user returns True for successfull auth, otherwise false'''

    user_data = request.json

    if User.authenticate(user_data['username'], user_data['password']):
        session['curr_user'] = user_data['username']
        return jsonify(True)

    return jsonify(False)
