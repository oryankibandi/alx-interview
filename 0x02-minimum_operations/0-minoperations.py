#!/usr/bin/python3
"""
calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""

global target
global multiplier
global value
global num_of_operations
    
def copy():
    """
    copies a character
    """
    global multiplier
    global value
    global num_of_operations

    multiplier = value
    num_of_operations += 1
    
def paste():
    """
    pastes copied characters
    """
    global value
    global multiplier
    global num_of_operations
    
    value += multiplier
    num_of_operations += 1
    
def compare():
    """Compares state"""
    global target
    global multiplier
    global value
    global num_of_operations
    
    if value == target:
        return num_of_operations
        
    if (target - value) % 2:
        paste()
        return compare()
    else:
        m = (target - value) / multiplier
        if isinstance(m, int):
            if m == 2:
                num_of_operations += 3
                return num_of_operations
            copy()
            paste()
            return compare()
        else:
            paste()
            return compare()


def minOperations(n: int) -> int:
    """calculates the fewest number of operations needed
    to result in exactly n H characters in the file."""
    global target
    global multiplier
    global value
    global num_of_operations
    
    if n == 0:
        return 0
    if n == 1:
        return 0

    target = n
    multiplier = 0
    value = 1
    num_of_operations = 0
    
    copy()
    paste()
    
    return compare()

