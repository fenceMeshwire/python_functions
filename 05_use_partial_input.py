#!/usr/bin/env python3

# Python 3.9.5

# 05_use_partial_input.py

# Purpose: Reduce the number of arguments to be passed to a function
# by using the partial() method from functools.

# Dependency
from functools import partial

def provide_data(fixed, variable_a, variable_b):
    return fixed, variable_a, variable_b

if __name__ == '__main__':
  
    fixed = 12
    sample = partial(provide_data, fixed)

    # Add variable data to the sample - consisting of a fixed and variable parts
    result = sample(25, 39)
    print(result)
