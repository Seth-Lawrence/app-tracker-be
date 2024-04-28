from flask import session

USER = 'curr_user'

class Auth:
    '''model for keeping users logged in / logging out through sessions'''

    @classmethod
    def do_login(user):
        '''logs user in, adds to session'''

        session[USER] = user.id

    @classmethod
    def logout_user():
        '''logs user out --> deletes user from sesison'''

        if USER in session:
            del session[USER]
