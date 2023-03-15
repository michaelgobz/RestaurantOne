"""db client"""
from sqlalchemy import create_engine

class DBClient:
    """postgresql db client"""
    def __init__(self, host, port, user, password, db, echo=False):
        self.__engine = create_engine(
            f"postgresql://{user}:{password}@{host}:{port}/{db}",
            echo=echo
        )

    def get_engine(self):
        """get engine"""
        return self.__engine

    def get_session(self):
        """get session"""
        return self.__engine.session()
    
    