from app_tracker.database import db
from sqlalchemy.orm import validates
from datetime import datetime

class User(db.Model):
    '''model for user class'''

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )

    username = db.Column(
        db.string(20),
        unique=True,
    )

    password = db.Column(
        db.string(),
    )

    @validates('password')
    def validate_password(self, password):
        '''validates pw to ensure it's not too short'''

        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long')






