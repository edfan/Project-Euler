import math

def primechecker(x):
    for y in range(2, int(math.floor(math.sqrt(x)) + 1)):
        if x % y == 0:
            return False
    return True

def permutationcheck(a, b, c):
    lista = []
    listb = []
    listc = []
    for x in str(a):
        lista.append(int(x))
    for x in str(b):
        listb.append(int(x))
    for x in str(c):
        listc.append(int(x))
    lista.sort()
    listb.sort()
    listc.sort()
    if lista == listb == listc:
        return True
    else:
        return False

for x in range(1000,10000):
    for y in range(1, (10000-x)/2):
        if permutationcheck(x, x+y, x+(2*y)) == True:
            if primechecker(x) == True and primechecker(x+y) == True and primechecker(x+(2*y)) == True:
                print([x, x+y, x+(2*y)])
                    
