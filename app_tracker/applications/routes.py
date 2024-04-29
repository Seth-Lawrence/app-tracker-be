from flask import Blueprint, jsonify, request
from sqlalchemy import exc

from app_tracker.users.models import User
from app_tracker.database import db


application = Blueprint('application', __name__)

@application.post('/new')
def create_application():
    '''adds application'''

    data = request.json
    username = data['username']

    user = User.query.filer(User.username == username).one_or_none()

    app = user.add_application(
        data['status'],
        data['company_name'],
        data['city'],
        data['state'],
        data['cover_letter'],
        data['remote'],
        data['app_received_confirm'],
        data['farthest_round_cat'],
        data['outreach'],
        data['outreach_response'],
        data['referral'],
        data['result_date'],
        data['min_pay'],
        data['max_pay'],
        data['outreach_date'],
        data['num_rounds_reached']
    )

    db.session.add(app)
    try:
        db.session.commit()
    except exc.IntegrityError:
        return jsonify(error='Error submitting application')

    return jsonify(app)


@application.post('/edit')
def edit_application():
    '''edits existing application'''



