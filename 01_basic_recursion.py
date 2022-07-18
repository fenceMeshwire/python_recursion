#!/usr/bin/env python3

# Python 3.9.5

# 01_basic_recursion.py

# The stack is a data structure that is modeled according to the last-in-first-out (LIFO) principle.

def use_recursive_function(int_number):
    # first if-condition is only to show the 'going-into-stack' process.
    if int_number > 0: print(int_number, ' -> going into stack...')
    # Last step / stopping condition:
    if int_number == 0:
        print(int_number, ' Base case.')
        return
    else:
        # Repeating step / working condition:
        use_recursive_function(int_number - 1)
        print(int_number, ' -> ...returning from stack')
        return

if __name__ == '__main__':
    int_number = int(5)
    use_recursive_function(int_number)
