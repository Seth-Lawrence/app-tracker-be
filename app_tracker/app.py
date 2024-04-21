from flask import Flask

from app_tracker.database import connect_db
from app_tracker.config import DATABASE_URL
from app_tracker.users.models import User
from app_tracker.applications.models import Application

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL



connect_db(app)
