from flask import Blueprint, jsonify, request
from datetime import datetime
from app_tracker.users.models import User
from app_tracker.database import db


application = Blueprint('application', __name__)

@application.post('/new')
def add_application(
    user:User,
    status: str,
    company_name: str,
    job_title: str,
    city: str,
    state: str,
    cover_letter: bool,
    remote: bool | None,
    app_recived_confirm: bool | None,
    farthest_round_cat: str,
    outreach: bool | None,
    outreach_response: bool | None,
    referral: bool | None,
    result_date: datetime | None,
    min_pay: int | None = None,
    max_pay: int | None = None,
    outreach_date: datetime | None = datetime,
    num_rounds_reached: int = 0
    ):
    '''adds application'''

    application_data = request.json

    app = user.add_application(application_data)

    db.session.add(app)
    db.session.commit()

    return jsonify(app)


@application.post('/edit')
def edit_application(application_id):
    '''edits existing application'''



