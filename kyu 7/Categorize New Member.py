# Explaination of problem here: https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa

def open_or_senior(data):
    list = []
    for d in data: 
        age = d[0]
        handicap = d[1]
        if age >= 55 and handicap > 7:
            list.append('Senior')
        else:
            list.append('Open')
            
    return list


# Thoughts and Aliternatives solutations

# Tests
