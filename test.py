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
    assert cache.list() == [(2, 20), (1, 10)], f"{cache.list()} != [(2, 20), (1, 10)]"
    assert cache.get(1) == 10
    assert cache.list() == [(1, 10), (2, 20)], f"{cache.list()} != [(1, 10), (2, 20)]"
    cache.put(3, 30)
    assert cache.list() == [(3, 30), (1, 10)], f"{cache.list()} != [(3, 30), (1, 10)]"
    assert cache.get(2) is None
    assert cache.list() == [(3, 30), (1, 10)], f"{cache.list()} != [(3, 30), (1, 10)]"
    cache.put(4, 40)
    assert cache.list() == [(4, 40), (3, 30)], f"{cache.list()} != [(4, 40), (3, 30)]"
    assert cache.get(1) is None
    assert cache.list() == [(4, 40), (3, 30)], f"{cache.list()} != [(4, 40), (3, 30)]"
    assert cache.get(3) == 30
    assert cache.list() == [(3, 30), (4, 40)], f"{cache.list()} != [(3, 30), (4, 40)]"
    assert cache.get(4) == 40
    assert cache.list() == [(4, 40), (3, 30)], f"{cache.list()} != [(4, 40), (3, 30)]"
    cache.put(3, 300)
    assert cache.list() == [(3, 300), (4, 40)], f"{cache.list()} != [(3, 300), (4, 40)]"
    cache.put(3, 3)
    assert cache.list() == [(3, 3), (4, 40)], f"{cache.list()} != [(3, 3), (4, 40)]"
        
    print("Test function completed successfully")

if __name__ == "__main__":
    print("Starting test.py")
    test()
    print("Done")