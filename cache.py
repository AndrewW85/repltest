"""
cache.py

Implement your Cache using the class skeleton provided below.
"""
from collections import OrderedDict
from typing import List, Optional, Dict, Tuple


class Cache:
    cache_capacity : int
    cache_items: Dict[int, int]
  
    def __init__(self, capacity: int):
        # Initialize the LRU cache with positive size capacity.
        self.cache_capacity = capacity
        self.cache_items = OrderedDict()
        

    def get(self, key: int) -> Optional[int]:
        # Return the value of the key if the key exists, otherwise returns None.
        try:
            self.cache_items.move_to_end(key, last=False)
        except KeyError:
            return None

        return self.cache_items.get(key, None)
             

    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if the key exists. Otherwise, add the 
        key-value pair to the cache. If the number of keys exceeds the capacity 
        from this operation, evict the least recently used key.
        """
        self.cache_items[key] = value
        self.cache_items.move_to_end(key, last=False)
        
        if len(self.cache_items) > self.cache_capacity:
            self.cache_items.popitem()
            
    def list(self) -> List[Tuple[int, int]]:
        """
        Return the items stored in the cache as a list ordered from most recent 
        update as the first element to least recent update as the last element
        """
        return list(self.cache_items.items())
        