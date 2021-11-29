# Kevala Infrastructure Team Coding Challenge

Your coding challenge is described below. Do your best to complete these tasks in the alloted time. If you have any questions about the task, you are free to ask for clarification. 

```
Implement a cache that will store a fixed number of key, value pairs.
If adding an item to the cache would cause the cache capacity be exceeded,
the cache must evict the least recently used item while storing the new
item.

Cache(capacity: int)
Initialize the LRU cache with positive size capacity.

get(key: int) -> Optional[int]
Return the value of the key if the key exists, otherwise returns None.

put(key: int, value: int) -> None
Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache. If the number of keys exceeds
the capacity from this operation, evict the least recently used key.

e.g.
cache = Cache(2)
cache.put(1, 1) # cache is {1: 1}
cache.put(2, 2) # cache is {1: 1, 2: 2}
cache.get(1)    # return 1
cache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1: 1, 3: 3}
cache.get(2) # returns None (not found)
cache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4: 4, 3: 3}
cache.get(1) # return None (not found)
cache.get(3) # return 3
cache.get(4) # return 4
```
