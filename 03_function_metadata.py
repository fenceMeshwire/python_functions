#!/usr/bin/env python3

# Python 3.9.5

# 03_function_metadata.py

# Purpose: Declare and provide input knowledge in order to provide a desired output.

def multiply(x:int, y:int) -> int:
    return x * y
  
# Return help on function multiply in module __main__:
help(multiply)
  
# Show annotations
multiply.__annotations__
