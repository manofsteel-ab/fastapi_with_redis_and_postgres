import redis
from core.config import settings

redis_client = redis.StrictRedis.from_url(settings.redis_url)
