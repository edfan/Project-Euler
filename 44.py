import math

def pentagonal(x):
    return x*(3*x-1)/2

pentas = []

for x in xrange(1, 5000):
    pentas.append(pentagonal(x))
    print(x)

d = 10000

for a in pentas:
    for b in pentas:
        if a+b in pentas and a-b in pentas and math.fabs(a-b) < d:
            d = math.fabs(a-b)
            print(d)

print(d)
