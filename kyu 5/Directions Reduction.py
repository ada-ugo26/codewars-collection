# Link to Problem Description: https://www.codewars.com/kata/550f22f4d758534c1100025a 

# Solution

def dir_reduc(arr):
    opp = {"NORTH": "SOUTH", 
           "SOUTH": "NORTH", 
           "EAST": "WEST", 
           "WEST": "EAST"}
    
    i = 0
    while i < len(arr) - 1:
        if arr[i + 1] == opp[arr[i]]:
            # Remove both elements
            arr.pop(i)
            arr.pop(i)
            # Move back to check previous element (if any)
            if i > 0:
                i -= 1
        else:
            i += 1
    
    return arr

# Thoughts and alternatives

# Tests
