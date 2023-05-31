""" The base controller for all controllers in the routes. """

import typing as Typing
from flask_jwt_extended import get_jwt, get_jwt_identity
                                


class BaseController:
    """ The base controller for all controllers in the routes. """
    _request = None
    _db_client = None
    _access_token: Typing.Optional[str] = None

    def __init__(self, request, db_client):  # noqa: F811
        """ The constructor for the base controller. """
        self.request = request
        self.db_client = db_client

    def get_request(self):
        """ The get method for the base controller. """
        return self.request
    
    def get_current_user(self):
        """ The get current user method for the base controller. """
        return get_jwt_identity()

    def get_access_token(self) -> str:
        """ The get access token method for the base controller. """
        token = get_jwt()['jti']
        self._access_token = token
        return self._access_token

    def get_db_client(self):
        """ The get db client method for the base controller. """
        return self.db_client
    
    def send_mail_message(self, email, subject, body):
        """ The send mail message method for the base controller. """
    
    