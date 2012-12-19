import math

def prime(x):
    for y in range(2, int(math.floor(math.sqrt(x)) + 1)):
        if x % y == 0:
            return False
    return True

primes = []
for x in xrange(2, 1000000):
    if prime(x) == True:
        primes.append(x)
        
currentmax = 0

for a in xrange(0, 78703):
    for b in xrange(a, 78703):
        if sum(primes[a:b]) in primes:
            if sum(primes[a:b]) > currentmax:
                currentmax = sum(primes[a:b])
                print(currentmax)

print(currentmax)

            
