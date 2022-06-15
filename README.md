# Kevala Infrastructure Team Coding Challenge

Your coding challenge is described below. Do your best to complete these tasks in the alloted time. If you have any questions about the task, you are free to ask for clarification. 

The repl has been setup to run your code with the following command: `python main.py`.  
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

list() -> List[int]
Return the items stored in the cache as a list ordered from most recent update as the 
first element to least recent update as the last element

e.g.
cache = Cache(2)
cache.put(1, 10)      # cache is [(1, 10)]
cache.put(2, 20)      # cache is [(2, 20), (1, 10)]
cache.get(1)          # return 10, cache is [(1, 10), (2, 20)]
cache.put(3, 30)      # cache is [(3, 30), (1, 10)]
cache.get(2)          # return None, cache is [(3, 30), (1, 10)]
cache.put(4, 40)      # cache is [(4, 40), (3, 30)]
cache.get(1)          # return None, cache is [(4, 40), (3, 30)]
cache.get(3)          # return 30, cache is [(3, 30), (4, 40)]
cache.get(4)          # return 40, cache is [(4, 40), (3, 30)]
cache.put(3, 300)     # cache is [(3, 300), (4, 40)]
cache.put(3, 3)       # cache is [(3, 30), (4, 40)]
```