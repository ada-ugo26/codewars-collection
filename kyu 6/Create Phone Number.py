# Link to Problem Description: https://www.codewars.com/kata/525f50e3b73515a6db000b83

# Solution

def create_phone_number(n):
    # Convert list of integers to string
    digits = ''.join(str(d) for d in n)
    
    # Format as phone number
    return f"({digits[0:3]}) {digits[3:6]}-{digits[6:]}"


# Thoughts and alternatives

# Tests
