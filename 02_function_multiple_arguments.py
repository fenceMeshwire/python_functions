#!/usr/bin/env python3

# 02_function_multiple_arguments_kwargs.py

# Python 3.9.5

# Example: Function representation. kwargs refers to keyword-only arguments
def function_representation(*args, **kwargs):
    print(args)     # returns a tuple
    print(kwargs)   # returns a dictionary
    return

# Alternative method to create a dictionary from 'kwargs'
def create_dict(**dictionary):
    return dictionary

dictionary = create_dict(key_1='value_1', key_2='value_2', key_3='value_3')
print(dictionary)   

# Result: {'key_1': 'value_1', 'key_2': 'value_2', 'key_3': 'value_3'}

# ============================ Example ============================

def create_record(ID, name, price, **data):
    print(data.values())
    additional_data = [item for item in data.values()] # Disolve the dictionary values
    additional_data = ','.join(additional_data)        # Join the dictionary values to a string
    record = str(ID) + ',' + name + ',' + str(price) + ',' + additional_data
    return record

if __name__ == '__main__':
    # To create the keyword-only arguments, variables have to be declared in order to build up the dictionary **data
    result = create_record(1, 'Tomato Soup', 2.5, weight='300g', manufacturer='Campbell', product='soup', origin='USA', rating='tasty')
    
    print(result)       # 1,Tomato Soup,2.5,300g,Campbell,soup,USA,tasty
    print(type(result)) # <class 'str'>
