""" accounts controller
     This module contains the accounts controller class
     """

from .base_controller import BaseController
from ..models import User


class AccountsController:
    """The accounts controller for all controllers in the api"""

    _controller: BaseController = None

    def __init__(self, controller: BaseController):
        """The constructor for the accounts controller."""
        self._controller = controller

    def get_controller(self):
        """The get method for the accounts controller."""
        return self._controller

    def get_accounts(self):
        """Get all accounts"""
        return self.get_controller().get_db_client().get_session().query(User).all()
