# read input
lines = open("input.txt", "r").readlines()

# calculate the score for a line
def score(line):
    first = line[:int(len(line)/2)]  # first compartment
    second = line[int(len(line)/2):] # second compartment
    items = dict()                   # dictionary of items in the first half
    count = 0                        # current count

    # for all items in the first half set that they're present in our items' dictionary
    # this should allow us to not have a quadratic time complexity assuming the lookup is O(1)
    for item in first:
        items[item] = True

    # for all items in the second half check if they're also present in the first half
    for item in second:
        if items.get(item):
            # calculate priority according to the rules of the game
            count += ord(item)-ord('A')+27 if item.isupper() else ord(item)-ord('a')+1
            # we don't need to consider this item anymore, set it false to skip duplicates
            items[item] = False
    return count

# return final result
print(sum([ score(x) for x in lines ]))