import math

def pentagon(x):
    return x*(3*x-1)/2

def pentacheck(x):
    if (math.sqrt(24*x+1)%6 == 5):
        return True
    return False

pents = []

for x in range(1, 5000):
    pents.append(pentagon(x))

for x in range(len(pents)):
    for y in range(x+1, len(pents)):
            if pentacheck(pents[y]-pents[x]) == True and pentacheck(pents[x]+pents[y]) == True:
                print(pents[x], " ", pents[y], " ", pents[x]-pents[y])

