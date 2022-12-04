# read input
lines = open("input.txt", "r").readlines()

# return if r1 is in r2
def in_range(r1, r2):
    return r1[0] >= r2[0] and r1[1] <= r2[1] 

# find if one of the two ranges is contained in the other
def overlap(line):
    # parse line
    pair = [ (int(x.split("-")[0]), int(x.split("-")[1])) for x in line.split(",") ]

    # check if one range is within the other or viceversa
    return 1 if in_range(pair[0], pair[1]) or in_range(pair[1], pair[0]) else 0

# return total
print(sum([overlap(line) for line in lines]))