from app_tracker.database import db
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

    @classmethod
    def register(self, username, name, password):

        hashed_pwd = generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            name=name,
            password=hashed_pwd,
        )

        print(user.password)
        print(user.username)

        db.session.add(user)
        db.session.commit()
