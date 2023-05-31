""" The base controller for all controllers in the routes. """

import typing as Typing
import requests
from  import db
from flask import Blueprint, abort, jsonify, redirect, request, url_for
from flask_jwt_extended import (create_access_token, get_jwt, get_jwt_identity,
                                )


class BaseController:
    """ The base controller for all controllers in the routes. """
    _request: Typing.Optional[requests.Request] = None
    _db_client: Typing.Optional[db] = None
    _access_token: Typing.Optional[str] = None

    def __init__(self, request, db):
        """ The constructor for the base controller. """
        self.request = request
        self.db_client = db

    def get_request(self) -> requests.Request:
        """ The get method for the base controller. """
        return self.request

    def get_access_token(self) -> str:
        """ The get method for the base controller. """
        token = get_jwt()['jti']
        self.access_token = token
        return self.access_token

    def get_db_client(self) -> db:
        """ The get method for the base controller. """
        return self.db_client


api_controller = BaseController(request, db)
