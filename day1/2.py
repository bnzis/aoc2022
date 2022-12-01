# read all the lines in the input file and put them in an array
lines = open("input.txt", "r")
totals = [] # total amount of calories for each elf
current = 0 # current amount summed

# similar to part one, put this time we don't care to find the maximum
# and just store the totals
for line in lines:
    if line == "\n":
        totals.append(current)
        current = 0
    else:
        current += int(line)
totals.sort(reverse=True) # sort in descending order
print(sum(totals[:3]))    # return sum of the first three elements