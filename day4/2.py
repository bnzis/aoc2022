# read input
lines = open("input.txt", "r").readlines()

# return if x is within the bounds of r
def in_range(x, r):
    return r[0] <= x <= r[1]

# find if the two ranges overlap at all
def overlap(line):
    # parse line
    pair = [ (int(x.split("-")[0]), int(x.split("-")[1])) for x in line.split(",") ]

    # check if they overlap
    return 1 if in_range(pair[0][0], pair[1]) or in_range(pair[1][0], pair[0]) else 0

# return total
print(sum([overlap(line) for line in lines]))