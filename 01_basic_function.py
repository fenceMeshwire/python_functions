#!/usr/bin/env python3

# Python 3.9.5

# 01_basic_function.py

def labor_decision(working_mood, ability, allowance):
    if working_mood == True and ability == True and allowance == True:
        work_result = True
    else:
        work_result = False
    return work_result

if __name__ == '__main__':
    working_mood = True
    ability = True
    allowance = True
    result = labor_decision(working_mood, ability, allowance)
    print(result)
