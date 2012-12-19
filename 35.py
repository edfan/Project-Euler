import math
primes = []
a = 1

for x in range(2, 1000000):
    primeness = 1
    while x - a > 1:
        if x % (x - a) == 0:
            primeness = 0
        a += 1
    if primeness == 1:
        primes.append(x)
    primeness = 1

for y in primes:
    currentlist = []
    for a in str(y):
        currentlist.append(int(a))
    
