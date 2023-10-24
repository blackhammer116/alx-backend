#!/usr/bin/env python3
"""
Creating a basic cache
"""

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from the parent(super) class
    BaseCaching and defines put() and get() method
    """
    def __init__(self):
        """
        __init__ function taken from base class
        """
        BaseCaching.__init__(self)

    def put(self, key, value):
        """
        A method that adds a new key value pair in the dictionary
        cache_data
        Args:
            key: key of the dictionary
            value: value of the dictionary
        """
        if key is not None:
            self.cache_data[key] = value

    def get(self, key):
        """
        A method that returns the value linked to
        the key in the dictionary cache_data
        Args:
            key: key of the dictionary
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
