from .client import RedisClient
from app import app

redis_client = RedisClient(app=app)

__all__ = ['redis_client']
