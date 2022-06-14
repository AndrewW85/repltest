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
    cache.put(1, 1)
    assert cache.list() == [1], f"{cache.list()} != [1]"
    cache.put(2, 2)
    assert cache.list() == [2, 1], f"{cache.list()} != [2, 1]"
    cache.get(1)
    assert cache.list() == [1, 2], f"{cache.list()} != [1, 2]"
    cache.put(3, 3)
    assert cache.list() == [3, 1], f"{cache.list()} != [3, 1]"
    cache.get(2)
    assert cache.list() == [3, 1], f"{cache.list()} != [3, 1]"
    cache.put(4, 4)
    assert cache.list() == [4, 3], f"{cache.list()} != [4, 3]"
    cache.get(1)
    assert cache.list() == [4, 3], f"{cache.list()} != [4, 3]"
    cache.get(3)
    assert cache.list() == [3, 4], f"{cache.list()} != [3, 4]"
    cache.get(4)
    assert cache.list() == [4, 3], f"{cache.list()} != [4, 3]"
    print("Test function completed successfully")

if __name__ == "__main__":
    print("Starting test.py")
    test()
    print("Done")