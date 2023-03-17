# Authentication module
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from api.core.base import Db as db
from api.db_models import User


def _hash_password(password: str) -> str:
    # returns hash of the password hashed with bcrypt.hashpw
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    return hashed

class Auth:
    # Authentication class to interact with the database
    def __init__(self):
        pass

    def register_user(self, email: str, password: str, **kwargs) -> User:
        """ Register a user in the db
        Returns a User object
        """
        try:
            user = User.query.filter_by(email=email).first()
            if user is None:
                raise NoResultFound
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = User(email, hashed_password, **kwargs)
            db.session.add(user)
            db.session.commit()

            return user

        else:
            raise ValueError(f'User with email {email} already exists')
        

    def valid_login(self, email: str, password: str) -> bool:
        """Returns True if email exists and password checked
        with bcrypt.checkpw and False otherwise
        """
        try:
            user = User.query.filter_by(email=email)
            if user is None:
                raise NoResultFound
        except NoResultFound:
            return False

        user_pwd = user.hashed_password
        encoded_pwd = password.encode()

        if bcrypt.checkpw(encoded_pwd, user_pwd):
            return True

        return False
