#!/usr/bin/env/ python3
""" Task 0"""
import redis
import uuid
import random
import string


class Cache:
    def __init__(self):
        # Initialize the Redis client and flush the database
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """
        Store the input data in Redis using a randomly generated key.

        Args:
            data: The data to be stored in the cache.

        Returns:
            key: The randomly generated key under which the data is stored.
        """
        # Generate a random key using UUID and convert it to a string
        random_key = str(uuid.uuid4())

        # Store the data in Redis using the generated key
        self._redis.set(random_key, data)

        return random_key
