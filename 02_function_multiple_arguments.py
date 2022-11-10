#!/usr/bin/env python3

# 02_function_multiple_arguments_kwargs.py

# Python 3.9.5

# Example: Function representation
# kwargs refers to keyword-only arguments
def function_representation(*args, **kwargs):
    print(args)     # returns a tuple
    print(kwargs)   # returns a dictionary
    return

def create_record(ID, name, price, **data):
    print(data.values())
    additional_data = [item for item in data.values()] # Disolve the dictionary values
    additional_data = ','.join(additional_data)        # Join the dictionary values to a string
    record = str(ID) + ',' + name + ',' + str(price) + ',' + additional_data
    return record

if __name__ == '__main__':
    # To create the keyword-only arguments, variables have to be declared in order to build up the dictionary **data
    create_record(1, 'Tomato Soup', 2.5, weight='300g', manufacturer='Campbell', product='soup', origin='USA', rating='tasty')
