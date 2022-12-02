# read input
lines = open("input.txt", "r").readlines()

# there's definitely a better way to do this... part 2 lol
def outcome(x):
    if x[2] == 'X':
        if x[0] == 'A':
            return 3
        elif x[0] == 'B':
            return 1
        else:
            return 2
    elif x[2] == 'Y':
        return (ord(x[0]) - ord('A')) + 4
    else:
        if x[0] == 'A':
            return 8
        elif x[0] == 'B':
            return 9
        else:
            return 7

# calculate the final score
score = sum([ outcome(x) for x in lines ])

# return final result
print(score)