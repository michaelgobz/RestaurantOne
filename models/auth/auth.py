""" Authentication module """
import bcrypt
from ..db.db import DB
from ..db.models import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from typing import Union


def _hash_password(password: str) -> str:
    """ Returns Bytes(salted hash of the input password)
    hashed with bcrypt.hashpw
    """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    return hashed


def _generate_uuid() -> str:
    """Returns a string representation of a new UUID
    """
    UUID = uuid4()
    return str(UUID)


class Auth:
    """Auth class to interact with the authentication database
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str, **kwargs) -> User:
        """ Register a user in the db
        Returns a User object
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password, **kwargs)

            return user

        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """Returns True if email exists and password checked
        with bcrypt.checkpw and False otherwise
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        user_pwd = user.hashed_password
        encoded_pwd = password.encode()

        if bcrypt.checkpw(encoded_pwd, user_pwd):
            return True

        return False

    def create_session(self, email: str) -> Union[str, None]:
        """ Returns a session id
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)

        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        """Returns string argument of the corresponding user or None
        """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

        return user

    def destroy_session(self, user_id: int) -> None:
        """ Updates the user's session ID to None
        """
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None

        user = self._db.update_user(user.id, session_id=None)

        return None

    def get_reset_password_token(self, email: str) -> str:
        """ Geneartes a UUID and updates the user's reset_token
        database field
        Returns the token
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        reset_token = _generate_uuid()
        user = self._db.update_user(user.id, reset_token=reset_token)

        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """ Updates password
        """
        if reset_token is None or password is None:
            return None

        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError

        hashed_pwd = _hash_password(password)
        self._db.update_user(user.id, hashed_password=hashed_pwd,
                             reset_token=None)