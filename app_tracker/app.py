from flask import Flask, session, g

from app_tracker.database import connect_db
from app_tracker.config import DATABASE_URL, SECRET_KEY
from app_tracker.users.routes import user
from app_tracker.users.models import User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SECRET_KEY'] = SECRET_KEY

USER = 'curr_user'


@app.before_request
def authorize():
    if USER in session:
        g.user = User.query.get(session[USER])

    else:
        g.user = None


def do_login(user):
    '''logs user in, adds to session'''

    session[USER] = user.id

def logout_user():
    '''logs user out --> deletes user from sesison'''

    if USER in session:
        del session[USER]

app.register_blueprint(user, url_prefix='/api/user')

connect_db(app)
