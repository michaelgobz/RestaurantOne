"""db client"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def _get_connection_string(host, port, user, password, db) -> str:
    """get connection string"""
    return f"postgresql://{user}:{password}@{host}:{port}/{db}"


class DBClient:
    """postgresql db client"""

    def __init__(self, host, port, user, password, db):
        self.__engine = SQLAlchemy()
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.__migrate = None

    def get_engine(self):
        """get engine instance tied to flask app"""
        return self.__engine

    def get_session(self):
        """get session"""
        return self.__engine.session()

    def get_migrate(self):
        """get migrate"""
        return self.__migrate

    def initialize_app(self, app=None):
        """initialize app"""
        app.config['SQLALCHEMY_DATABASE_URI'] = \
            _get_connection_string(self.host, self.port, self.user,
                                        self.password, self.db)
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        self.__engine.init_app(app)
        self.__migrate = Migrate(app, self.__engine)
