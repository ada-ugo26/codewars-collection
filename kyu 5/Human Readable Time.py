# Explaination of problem here: https://www.codewars.com/kata/52685f7382004e774f0001f7

def make_readable(seconds):
    hours = 0
    minutes = 0
    if seconds in range(0,60):
            return f"00:00:{seconds:02d}"
    while seconds not in range(0,60):
        # keep minusing 60 and add one to minutes, if minutes is above 59, then minue 60 from minute and add 1 to hour
        seconds = seconds - 60
        minutes = minutes + 1
        if minutes not in range(60):
            minutes -= 60
            hours += 1

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


# Thoughts and Alternatives

# Tests

