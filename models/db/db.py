"""DB module
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from account.user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine(os.getenv('DATABASE_URI'), echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Saves the user to the database and
        Returns a User object
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()

        return new_user

    def find_user_by(self, **kwargs) -> User:
        """ Returns the first row found in the users table
        as filtered by the methods input arguments
        """
        if not kwargs:
            raise InvalidRequestError

        column_keys = User.__table__.columns.keys()

        for key in kwargs.keys():
            if key not in column_keys:
                raise InvalidRequestError

        user = self._session.query(User).filter_by(**kwargs).first()

        if user is None:
            raise NoResultFound

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Locate user to update and update the user's attributes
        as passed in the method's argument, then commit the changes
        to the database
        """
        if not kwargs:
            return None

        user = self.find_user_by(id=user_id)

        column_keys = User.__table__.columns.keys()

        for key in kwargs.keys():
            if key not in column_keys:
                raise ValueError

        for key, value in kwargs.items():
            setattr(user, key, value)

        self._session.commit()