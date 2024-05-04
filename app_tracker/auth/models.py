from flask import session
from app_tracker.config import USER


class Auth:
    '''model for keeping users logged in / logging out through sessions'''

    @classmethod
    def do_login(self, user: object) -> None:
        '''takes username and adds to session  to keep user in session'''

        session[USER] = user.id

    @classmethod
    def logout_user(self) -> None:
        '''logs user out --> deletes user from sesison'''

        if USER in session:
            del session[USER]
