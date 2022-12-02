# read input
lines = open("input.txt", "r").readlines()

# there's definitely a better way to do this...
def outcome(x):
    if (x[2] == 'X' and x[0] == 'C') or (x[2] == 'Y' and x[0] == 'A') or (x[2] == 'Z' and x[0] == 'B'):
        return 6
    elif (x[2] == 'Z' and x[0] == 'A') or (x[2] == 'X' and x[0] == 'B') or (x[2] == 'Y' and x[0] == 'C'):
        return 0
    else:
        return 3

# calculate the final score
score = sum([ outcome(x) + (ord(x[2])-ord('W')) for x in lines ])

# return final result
print(score)