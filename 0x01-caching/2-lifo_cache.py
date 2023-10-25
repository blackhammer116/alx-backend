#!/usr/bin/env python3
"""
Creating a caching Module that implements FIFO
islice: to determine the index in a dictionary
"""
from itertools import islice

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    A caching class that implements a FIFO algorithim
    """
    def __init__(self):
        """
        __init__ method overloaded from the base class
        """
        super().__init__()

    def put(self, key, item):
        """
        A method that adds a new key value pair to the dict
        by first checking whether the allowed limit is passed or
        not
        Args:
            key: key on the new item
            item: value of the new key
        """
        if key is not None and item is not None:
            if len(self.cache_data) < self.MAX_ITEMS:
                self.cache_data[key] = item
            else:
                #i = list(self.cache_data.keys())[list(self.cache_data).index()]
                #r = self.cache_data.\
                 #       pop(next(islice(self.cache_data, (len(self.cache_data) - 1), None)))
                i = next(islice(self.cache_data, (len(self.cache_data) - 1), None))
                k = list(self.cache_data.keys())[list(self.cache_data).index(i)]
                del self.cache_data[i]
                self.cache_data[key] = item
                print(f"DISCARD: {k}")
                #print("DISCARD: {}".\
                 #       format(list(self.cache_data.\
                  #      keys())[list(self.cache_data.values()).index(r)]))

    def get(self, key):
        """
        A method that returns the value linked to the key passed
        Args:
            key: key in the dict
        """
        if key is not None or key in self.cache_data:
            return self.cache_data[key]
        return None
