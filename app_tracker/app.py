from flask import Flask

from app_tracker.database import connect_db
from app_tracker.config import DATABASE_URL, SECRET_KEY
from app_tracker.users.routes import user


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(user, url_prefix='/api/user')

connect_db(app)
