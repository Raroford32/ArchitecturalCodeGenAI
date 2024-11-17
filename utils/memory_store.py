import redis
import json
import logging
from typing import Optional, Any
from config import REDIS_HOST, REDIS_PORT, REDIS_DB

class MemoryStore:
    """Redis-based memory store for managing application state"""
    
    def __init__(self):
        """Initialize Redis connection with retry logic"""
        self.logger = logging.getLogger(__name__)
        self._connect_with_retry()

    def _connect_with_retry(self, max_retries: int = 3) -> None:
        """
        Establish Redis connection with retry logic
        
        Args:
            max_retries (int): Maximum number of connection attempts
            
        Raises:
            Exception: If connection fails after max retries
        """
        for attempt in range(max_retries):
            try:
                self.client = redis.Redis(
                    host=REDIS_HOST,
                    port=REDIS_PORT,
                    db=REDIS_DB,
                    decode_responses=True,  # Automatically decode response bytes to str
                    socket_timeout=5,  # Socket timeout in seconds
                    socket_connect_timeout=5,
                )
                # Test connection
                self.client.ping()
                self.logger.info("Successfully connected to Redis")
                return
            except redis.ConnectionError as e:
                self.logger.warning(f"Redis connection attempt {attempt + 1} failed: {str(e)}")
                if attempt == max_retries - 1:
                    raise Exception("Failed to connect to Redis after maximum retries")

    def save(self, key: str, value: Any) -> bool:
        """
        Save a value to Redis with automatic serialization
        
        Args:
            key (str): Redis key
            value (Any): Value to store (will be JSON serialized if not string)
            
        Returns:
            bool: True if successful
        """
        try:
            if not isinstance(value, str):
                value = json.dumps(value)
            self.client.set(key, value)
            return True
        except Exception as e:
            self.logger.error(f"Error saving to Redis: {str(e)}")
            return False

    def retrieve(self, key: str) -> Optional[str]:
        """
        Retrieve a value from Redis
        
        Args:
            key (str): Redis key
            
        Returns:
            Optional[str]: Retrieved value or None if not found
        """
        try:
            value = self.client.get(key)
            if value is None:
                self.logger.warning(f"No value found for key: {key}")
                return None
            return value
        except Exception as e:
            self.logger.error(f"Error retrieving from Redis: {str(e)}")
            return None

    def delete(self, key: str) -> bool:
        """
        Delete a key from Redis
        
        Args:
            key (str): Redis key to delete
            
        Returns:
            bool: True if successful
        """
        try:
            self.client.delete(key)
            return True
        except Exception as e:
            self.logger.error(f"Error deleting from Redis: {str(e)}")
            return False

    def clear_all(self) -> bool:
        """
        Clear all keys in the current Redis database
        
        Returns:
            bool: True if successful
        """
        try:
            self.client.flushdb()
            self.logger.info("Successfully cleared Redis database")
            return True
        except Exception as e:
            self.logger.error(f"Error clearing Redis database: {str(e)}")
            return False

    def __del__(self):
        """Ensure Redis connection is closed on object destruction"""
        try:
            self.client.close()
        except:
            pass
