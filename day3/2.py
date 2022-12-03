# read input
lines = open("input.txt", "r").readlines()

# compute score for a group
def score(x0,x1,x2):
    # dictionaries for the first two elves
    items0 = dict()
    items1 = dict()
    
    # set up the dictionaries with what elements are present, this should allow us
    # to avoid a O(nˆ3) time complexity assuming the lookup is O(1)
    for item in x0:
        items0[item] = True
    for item in x1:
        items1[item] = True

    # check what item is present in all three
    for item in x2:
        if items0.get(item) and items1.get(item):
            # returns priority
            return ord(item)-ord('A')+27 if item.isupper() else ord(item)-ord('a')+1
    # in case there's none...
    return 0

# returns final score
print(sum([ score(lines[x*3],lines[x*3+1],lines[x*3+2]) for x in range(int(len(lines)/3))]))