# Link to Problem Description: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

# Solution

def duplicate_encode(word):
    # Split word into chars
    chars = list(word.lower())
    newstr = []
    # for each char, check if char comes up more than once 
    for c in chars:
        if chars.count(c) > 1: # if so, add '(' to the use array
            newstr.append(")")
        else:
            newstr.append("(")# if not, add ')' to the newstr

    return "".join(newstr)


# Thoughs and alternatives

# Tests

