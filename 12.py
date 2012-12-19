import math
triangle = []
last = 0

for x in range(1, 100000):
    triangle.append(last + x)
    last = last + x

answer = 0
correct = 0
currentmaximum = 0

for x in triangle:
    if correct == 0:
        divisors = 0
        a = math.floor(math.sqrt(x))
        while a > 0:
            if x % a == 0:
                divisors += 1
            a -= 1
        divisors *= 2
        if math.floor(math.sqrt(x)) == math.sqrt(x):
            divisors -= 1
        if divisors > currentmaximum:
            currentmaximum = divisors
            print(currentmaximum)
        if divisors >= 500:
            correct = 1
            answer = x

print(answer)

