#!/usr/bin/env python3

# Python 3.9.5

# 03_binary_search.py

def binary_search(item, inventory, left=None, right=None):
    # By default, 'left' and 'right' ar all of 'inventory'
    if left is None:
        left = 0 # 'left' defaults to the 0 index
    if right is None:
        right = len(inventory) - 1 # 'right' defaults to the last index
    
    print('Progress:', inventory[left:right + 1])

    if left > right: # LAST STEP
        return None # The item is not listed in the inventory

    mid = (left + right) // 2
    if item == inventory[mid]: # LAST STEP
        return mid # The 'item' has been found in 'inventory'
    elif item < inventory[mid]: # REPEATING STEP
        return binary_search(item, inventory, left, mid - 1)
    elif item > inventory[mid]: # REPEATING STEP
        return binary_search(item, inventory, mid + 1, right)

if __name__ == '__main__':
    item = 21
    inventory = [1, 2, 3, 8, 11, 14, 17, 21, 25]
    binary_search(item, inventory)
