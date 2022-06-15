"""
test.py

This file provides a simple test of correctness for your solution. Tests are not 
required in this coding challenge. If using unit tests helps you, you can use the
Python unittest module which is supported by repl.it.
"""
from cache import Cache

def test():
    # Do not modify the contents of test(), but you are free to run this function to
    # check if your solution is correct.
    print("Running test function")
    
    cache = Cache(2)
    cache.put(1, 10)
    assert cache.list() == [(1, 10)], f"{cache.list()} != [10]"
    cache.put(2, 20)
    assert cache.list() == [(2, 20), (1, 10)], f"{cache.list()} != [20, 10]"
    cache.get(1)
    assert cache.list() == [(1, 10), (2, 20)], f"{cache.list()} != [10, 20]"
    cache.put(3, 30)
    assert cache.list() == [(3, 30), (1, 10)], f"{cache.list()} != [30, 10]"
    cache.get(2)
    assert cache.list() == [(3, 30), (1, 10)], f"{cache.list()} != [30, 10]"
    cache.put(4, 40)
    assert cache.list() == [(4, 40), (3, 30)], f"{cache.list()} != [40, 30]"
    cache.get(1)
    assert cache.list() == [(4, 40), (3, 30)], f"{cache.list()} != [40, 30]"
    cache.get(3)
    assert cache.list() == [(3, 30), (4, 40)], f"{cache.list()} != [30, 40]"
    cache.get(4)
    assert cache.list() == [(4, 40), (3, 30)], f"{cache.list()} != [40, 30]"
    print("Test function completed successfully")

if __name__ == "__main__":
    print("Starting test.py")
    test()
    print("Done")