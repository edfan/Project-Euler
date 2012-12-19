import math

def pandigitalchecker(x):
    currentnum = []
    for y in str(x):
        currentnum.append(int(y))
    currentnum.sort()
    if currentnum == [1, 2, 3, 4, 5, 6, 7]:
        return True
    else:
        return False

def primechecker(x):
    for y in range(2, math.floor(math.sqrt(x))):
        if x % y == 0:
            return False
    return True

currentmax = 0

for x in range(7612345, 7654322):
    if primechecker(x) == True and pandigitalchecker(x) == True and x > currentmax:
        currentmax = x
        print(x)

print(currentmax)
