from redis import StrictRedis

from settings import redis_settings

class BaseRedis():
    redis: StrictRedis

    def __init__(self):
        self.redis = StrictRedis(
            host=redis_settings.host,
            port=redis_settings.port,
            charset=redis_settings.charset,
            decode_responses=True
        )
