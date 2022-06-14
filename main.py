#!/usr/bin/env python

"""
Kevala Infrastructure Team Interview Challenge - Software Engineer

Instructions for your coding challenge are presented in the README.md file

Use this file, main.py, as the entrypoint for executing your code. A main() 
function has been provided to illistrate the class and method names and signatures.

You are free to implement your solution however you like as long as the API does not
change. At the end, test() will be run to verify the correctness of your solution
"""
from cache import Cach


def main():
    # You are free to modify the contents of main() for testing during development
    print("Running main function")
    cache = Cache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    cache.get(2)
    cache.put(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)
    print("Main function completed successfully")

  
if __name__ == "__main__":
    print("Starting main.py")
    main()
    print("Done")
