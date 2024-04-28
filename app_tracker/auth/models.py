from flask import session

USER = 'curr_user'

class Auth:
    '''model for keeping users logged in / logging out through sessions'''

    @classmethod
    def do_login(self, username:str) -> None:
        '''
        takes username and adds to session
        to keep user in session
        '''

        session[USER] = username

    @classmethod
    def logout_user(self) -> None:
        '''logs user out --> deletes user from sesison'''

        if USER in session:
            del session[USER]
