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