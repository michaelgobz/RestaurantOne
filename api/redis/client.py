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
    
    def update_payload(self, key, info):
        """ update the cached payload"""
        pass
    
    def delete_topic(self, key):
        """ delete the topic"""
        pass
    
    def get_topics(self):
        """ get all topics"""
        pass
    def get_topic(self, key):
        """ get a topic"""
        pass
    
    def get_topic_info(self, key):
        """ get a topic info"""
        pass
    
    def get_topic_payload(self, key):
        """ get a topic payload"""
        pass
    
    def get_topic_payload_info(self, key):
        """ get a topic payload info"""
        pass
    
    def get_redis_info(self):
        """ get redis info"""
        pass
    
        