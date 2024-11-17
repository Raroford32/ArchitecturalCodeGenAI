import redis
from config import REDIS_HOST, REDIS_PORT, REDIS_DB

class MemoryStore:
    def __init__(self):
        self.client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=REDIS_DB
        )

    def save(self, key, value):
        self.client.set(key, value)

    def retrieve(self, key):
        value = self.client.get(key)
        return value.decode('utf-8') if value else None

    def delete(self, key):
        self.client.delete(key)

    def clear_all(self):
        self.client.flushdb()
