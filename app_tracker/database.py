from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """connect to database"""

    app.app_context().push()
    db.app=app
    db.init_app(app)
