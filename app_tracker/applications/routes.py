from flask import Blueprint, jsonify, request
from sqlalchemy import exc

from app_tracker.users.models import User
from app_tracker.database import db


application = Blueprint('application', __name__)

@application.post('/new')
def create_application():
    '''adds application'''

    app_data = request.json
    username = app_data['username']

    user = User.query.filer(User.username == username).one_or_none()

    app = user.add_application(app_data)

    db.session.add(app)
    try:
        db.session.commit()
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(error='Error submitting application')

    serialized_app = app.serialize()

    return jsonify(app = serialized_app)

@application.post('/edit')
def edit_application():
    '''edits existing application'''
