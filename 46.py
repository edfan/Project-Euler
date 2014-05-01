import math
primes = []

for x in range(2, 6000):
    primeness = 0
    a = math.floor(math.sqrt(x))
    while a > 1:
        if x % a == 0:
            primeness = 1
        a -= 1
    if primeness == 0:
        primes.append(x)

doublesquare = []

for x in range(60):
    doublesquare.append(2*(x**2))

def check(x):
    for a in primes:
        if (x-a) in doublesquare:
            return False
    return True

for x in range(9, 6000, 2):
    if check(x)==True:
        print(x)
                
