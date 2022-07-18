#!/usr/bin/env python3

# Python 3.9.7

# 02_reverse_input.py

def reverse_input(given_string):
  
  # Last step, stopping condition:
  if len(given_string) == 0 or len(given_string) == 1:
    return given_string
  
  # Repeating step, working condition:
  else:
    first = given_string[0]
    rest = given_string[1:]
    # Values of variable "first" are stacking up reversed 
    # with each repetition:
    return reverse_input(rest) + first

if __name__ == '__main__':
    print(reverse_input('1234567'))
    # result: '7654321'
