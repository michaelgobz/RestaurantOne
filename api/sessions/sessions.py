from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from typing import Union

from api.db_models import User
from api.core.base import Db as db


def _generate_uuid() -> str:
    # Returns a string representation of a new UUID
    
    UUID = uuid4()
    return str(UUID)

class Session:
    # Manage session
    def create_session(self, email: str) -> Union[str, None]:
        #  Returns a session id
        
        try:
            user = User.query.filter_by(email=email)
            if user is None:
                raise NoResultFound
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        User.query.filter_by(id=user.id)

        setattr(user, session_id=session_id)

        db.session.commit()

        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        # Returns string argument of the corresponding user or None
        
        if session_id is None:
            return None

        try:
            user = User.query.filter_by(session_id=session_id)
            if user is None:
                raise NoResultFound
        except NoResultFound:
            return None

        return user

    def destroy_session(self, user_id: int) -> None:
        #  Updates the user's session ID to None
        
        try:
            user = User.query.filter_by(id=user_id)
            if user is None:
                raise NoResultFound
        except NoResultFound:
            return None

        setattr(user, session_id=None)

        db.session.commit()

        return None