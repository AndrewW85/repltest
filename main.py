#!/usr/bin/env python

"""
Kevala Infrastructure Team Interview Challenge - Software Engineer

Use this file, main.py, as an entrypoint for executing your code. A main() function has been provided as an example 
class and method names and method signatures. You are free to modify this code as long as the API does not break
with your changes
"""

def main():
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
  
  
if __name__ == "__main__":
  print("Starting")
  main()
  print("Done")
