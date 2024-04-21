from flask import Blueprint, jsonify, request
from app_tracker.database import db
from app_tracker.users.models import User

user = Blueprint('user',__name__)

@user.post('/register')
def register_user(username, password):
    '''calls register user on the api and registers the user'''

    User.register_user(username=username, password=password)
