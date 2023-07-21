""" redis client """
from flask_redis import FlaskRedis

class RedisClient():
    """ redis client """
    def __init__(self, app = None):
        self.__redis = FlaskRedis()
        self.__redis.init_app(app)

    def get_redis(self):
        """ get redis instance tied to flask app """
        return self.__redis
    
    def get_user(self):
        """ get user"""
        pass
    def create_topic(self, key, info):
        """ create a topic"""
        pass
    def retrieve_payload(self, key):
        """ return the cached pay load"""
        pass
    
        