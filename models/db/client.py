"""db client"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

class DBClient:
    """postgresql db client"""
    def __init__(self, host, port, user, password, db, app):
        self.__engine = SQLAlchemy()
        self.__connection_string = self._get_connection_string(host, 
                                                               port, user, password, db)
        app.config['SQLALCHEMY_DATABASE_URI'] = self.__connection_string
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.__engine.init_app(app)
        self.__migrate = Migrate(app, self.__engine)
        

    def get_engine(self):
        """get engine instance tied to flask app"""
        return self.__engine

    def get_session(self):
        """get session"""
        return self.__engine.session()
    
    def get_migrate(self):
        """get migrate"""
        return self.__migrate
    
    def _get_connection_string(self, host, port, user, password, db) -> str:
        """get connection string"""
        return f"postgresql://{user}:{password}@{host}:{port}/{db}"
    
    