""" The base controller for all controllers in the routes. """

import typing as Typing
from flask import Blueprint, abort, jsonify, redirect, request, url_for
from flask_jwt_extended import (create_access_token, get_jwt, get_jwt_identity,
                                )


class BaseController:
    """ The base controller for all controllers in the routes. """
    _request = None
    _db_client = None
    _access_token: Typing.Optional[str] = None

    def __init__(self, request, db):
        """ The constructor for the base controller. """
        self.request = request
        self.db_client = db

    def get_request(self):
        """ The get method for the base controller. """
        return self.request

    def get_access_token(self) -> str:
        """ The get access token method for the base controller. """
        token = get_jwt()['jti']
        self.access_token = token
        return self.access_token

    def get_db_client(self):
        """ The get db client method for the base controller. """
        return self.db_client

