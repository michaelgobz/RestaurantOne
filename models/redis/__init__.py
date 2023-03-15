from client import RedisClient

redis_client = RedisClient(host='localhost', port=6379, db=0, password='')

__all__ = ['redis_client']
