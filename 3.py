import math
primes = []

for x in range(2, 800000):
    primeness = 0
    a = math.floor(math.sqrt(x))
    while a > 1:
        if x % a == 0:
            primeness = 1
        a -= 1
    if primeness == 0:
        primes.append(x)
        print(x)

answers = []

for x in primes:
    if 600851475143 % x == 0:
        answers.append(x)

print(answers)
