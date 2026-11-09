# Link to Problem Description: https://www.codewars.com/kata/52597aa56021e91c93000cb0

# Solution

def move_zeros(lst):
    newlst = []
    zero_count = 0
    
    for num in lst:  # num is the actual value
        if num != 0:
            newlst.append(num)  # Add non-zero numbers
        else:
            zero_count += 1  # Count zeros
    
    # Append zeros at the end
    newlst.extend([0] * zero_count)
    
    return newlst


# Thoughs and alternatives

# Tests
