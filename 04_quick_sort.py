#!/usr/bin/env python3

# Python 3.9.5

# 04_quick_sort.py

# Initial situation:
# to_be_sorted = [8, 7, 6, 3, 1, 2, 5, 4, 9, ...]
# indices_tbs =  [0, 1, 2, 3, 4, 5, 6, 7, 8, ...]

def quick_sort(items, left=None, right=None):
    # Describe the lower and upper boundaries
    if left == None:
        left = 0 # lower boundary
    if right == None:
        right = len(items) - 1 # upper boundary

    if right <= left:
        return # LAST STEP
    
    index = left
    comparative = items[right]

    for value in range(left, right):
        # Swap the values if they're less or equal to the comparative:
        if items[value] <= comparative:
            items[index], items[value] = items[value], items[index]
            index = index + 1
    
    # The last item becomes the first item of the 'second half',
    # depending on the value of 'value'.
    items[index], items[right] = items[right], items[index]

    # Recursive calls of the quicksort functions as long the array needs to be sorted.
    quick_sort(items, left, index - 1)  # 'Left' side - REPEATING STEP
    quick_sort(items, index + 1, right) # 'Right' side - REPEATING STEP

if __name__ == '__main__':
    to_be_sorted = [8, 7, 6, 3, 1, 2, 5, 4, 9, 10, 11, 0]
    quick_sort(to_be_sorted)
    sorted = to_be_sorted
    print(sorted)
