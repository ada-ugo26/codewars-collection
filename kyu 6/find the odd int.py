# Link to Problem Description: https://www.codewars.com/kata/54da5a58ea159efa38000836

# Solution

def find_it(seq):
    # Create dict to track numbers
    numbers = {
        
    }
    
    for s in seq: # Track instances of a number in the array 
        if s in numbers:
            numbers[s] += 1
        else:
            numbers[s] = 1
        
    
    for key, value in numbers.items(): # return key with the odd number
        if value % 2 == 1:
            return key

# Thoughts and alternatives

# Tests

