# Link to Problem Description: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

# Solution

def persistence(n):
    # if n is a single digit, return 0
    if n < 10:
        return 0
    else:
        digits = [int(i) for i in str(n)]
        result = 1
        for d in digits:
            result = result * d
        return 1 + persistence(result)
    # if not, break number into digits and mulitply together and enter result back into function


# Thoughts and alternatives

# Tests
