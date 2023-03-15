""" redis client """
from redis import client

class RedisClient(client.Redis):
    """ redis client """
    def __init__(self, host, port, db, password):
        super().__init__(host=host, port=port, db=db, password=password)

    def set(self, key, value, ex=None, px=None, nx=False, xx=False):
        """ set key value """
        return super().set(key, value, ex=ex, px=px, nx=nx, xx=xx)

    def get(self, key):
        """ get key value """
        return super().get(key)

    def delete(self, key):
        """ delete key """
        return super().delete(key)

    def exists(self, key):
        """ check key exists """
        return super().exists(key)

    def expire(self, key, time):
        """ set key expire time """
        return super().expire(key, time)

    def ttl(self, key):
        """ get key expire time """
        return super().ttl(key)

    def hset(self, name, key, value):
        """ set hash key value """
        return super().hset(name, key, value)

    def hget(self, name, key):
        """ get hash key value """
        return super().hget(name, key)

    def hdel(self, name, key):
        """ delete hash key """
        return super().hdel(name, key)

    def hgetall(self, name):
        """ get all hash key value """
        return super().hgetall(name)

    def hkeys(self, name):
        """ get all hash key """
        return super().hkeys(name)

    def hlen(self, name):
        """ get hash length """
        return super().hlen(name)

    def hexists(self, name, key):
        """ check hash key exists """
        return super().hexists(name, key)

    def sadd(self, name, *values):
        """ add set value """
        return super().sadd(name, *values)

    def smembers(self, name):
        """ get all set value """
        return super().smembers(name)

    def srem(self, name, *values):
        """ remove set value """
        return super().srem(name, *values)

    def scard(self, name):
        """ get set length """
        return super().scard(name)

    def sismember(self, name, value):
        """ check set value exists """
        return