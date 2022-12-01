# read all the lines in the input file and put them in an array
lines = open("input.txt", "r").readlines()
current = 0 # current amount of calories summed
maximum = 0 # maximum total found

# then, line by line do:
for line in lines:
    # if the line is empty, it means we are dealing with a new elf
    if line == "\n":
        # check if we found a new maximum and continue
        maximum = current if current > maximum else maximum
        current = 0
    else:
        # otherwise, just keep summing
        current += int(line)

print(maximum) # return max