"""
cache.py

Implement your Cache using the class skeleton provided below
"""
from typing import List, Optional


class Cache:
    def __init__(self, capacity: int):
        # Initialize the LRU cache with positive size capacity.
        ...

    def get(self, key: int) -> Optional[int]:
        # Return the value of the key if the key exists, otherwise returns None.
        ...

    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if the key exists. Otherwise, add the 
        key-value pair to the cache. If the number of keys exceeds the capacity 
        from this operation, evict the least recently used key.
        """
        ...

    def list(self) -> List[int]:
        """
        Return the items stored in the cache as a list ordered from most recent 
        update as the first element to least recent update as the last element
        """
        ...