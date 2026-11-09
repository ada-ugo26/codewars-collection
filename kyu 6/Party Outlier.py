# Problem Description : https://www.codewars.com/kata/5526fc09a1bbd946250002dc

# Solution

def find_outlier(integers):
    # Create arrays
    oddNums = []
    evenNums = []
    
    for i in integers:
        if i % 2 != 1:
            oddNums.append(i)
        else:
            evenNums.append(i)
    
    # Return number with only 'one number'
    if len(oddNums) == 1:
        return oddNums[0]
    else:
        return evenNums[0]

# Thoughts and alternatives

# Tests


