#!/usr/bin/env/ python3
"""
Exercise
"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """
        Define Cache init
        """
        self._redis = redis.Redis()
        self._redis.flushdb()  # Flush the Redis instance

    def store(self, data):
        """
        Store data and self
        """
        key = str(uuid.uuid4())  # Generate a random key
        self._redis.set(key, data)  # Store the data in Redis
        return key
