from app_tracker.database import db
from sqlalchemy.orm import validates
from flask_bcrypt import Bcrypt, generate_password_hash

bcrypt = Bcrypt()

class User(db.Model):
    '''model for user class'''

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )

    name = db.Column(
        db.String(20),
        nullable=True,
    )

    username = db.Column(
        db.String(20),
        unique=True,
    )

    password = db.Column(
        db.String(),
    )

    @validates('password')
    def validate_password(self, key, password):
        '''validates pw to ensure it's not too short'''

        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long')

    @classmethod
    def register(self, username, name, password):

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')
        print(hashed_pwd)

        user = User(
            username=username,
            name = name,
            password=hashed_pwd
        )

        db.session.add(user)
        db.session.commit()
