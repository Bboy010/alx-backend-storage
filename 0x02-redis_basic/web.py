#!/usr/bin/env python3
""" cache and track"""
import requests
import redis


class WebCache:
    def __init__(self):
        """initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def get_page(self, url: str) -> str:
        # Track URL access count
        count_key = f"count:{url}"
        self._redis.incr(count_key)

        # Try to retrieve cached content
        cached_content = self._redis.get(url)
        if cached_content:
            return cached_content.decode("utf-8")

        # Fetch content from the URL
        response = requests.get(url)
        content = response.text

        # Cache content with a 10-second expiration
        self._redis.setex(url, 10, content)

        return content
