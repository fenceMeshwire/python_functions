#!/usr/bin/env python3

# Python 3.9.5

# 04_function_default_parameters.py

# Purpose: Setting default input parameters for a function.

def get_part(id, partname, qty=1):
    if qty == 1:
        query = f"Get {qty} unit from part {partname} with {id}."
    else:
        query = f"Get {qty} units from part {partname} with {id}."
    return query

if __name__ == '__main__':
    partname = 'washers'
    id = 1723
    # Quantity qty is not specified, so the function 
    # assigns qty=1 automatically
    get_part(id, partname)
