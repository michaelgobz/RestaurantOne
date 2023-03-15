"""db client"""
from flask_sqlalchemy import SQLAlchemy
from app import app

class DBClient:
    """postgresql db client"""
    def __init__(self, host, port, user, password, db):
        self.__engine = SQLAlchemy()
        self.__connection_string = self._get_connection_string(host, 
                                                               port, user, password, db)
        app.config['SQLALCHEMY_DATABASE_URI'] = self.__connection_string
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.__engine.init_app(app)
        

    def get_engine(self):
        """get engine instance tied to flask app"""
        return self.__engine

    def get_session(self):
        """get session"""
        return self.__engine.session()
    
    def _get_connection_string(self, host, port, user, password, db) -> str:
        """get connection string"""
        return f"postgresql://{user}:{password}@{host}:{port}/{db}"
    
    