from flask import Blueprint, jsonify, request
from app_tracker.database import db
from app_tracker.auth.models import Auth
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


@user.post('/login')
def login():
    '''signs in user returns True for successfull auth, otherwise false'''

    user_data = request.json
    user = User.authenticate(user_data['username'], user_data['password'])

    serialized_user = user.serialize()

    if user:
        Auth.do_login(user)

        return jsonify(user=serialized_user)

    return jsonify(error = 'incorrect username or password')


@user.post('/logout')
def logout():
    '''logs user out'''

    Auth.logout_user()

    return jsonify(logout=True)
