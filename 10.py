import math
primes = []

for x in range(2, 2000000):
    primeness = 0
    a = math.floor(math.sqrt(x))
    while a > 1:
        if x % a == 0:
            primeness = 1
        a -= 1
    if primeness == 0:
        primes.append(x)
        print(x)

print(sum(primes))
