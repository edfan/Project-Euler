import math

def factoring(x):
    lowerhalf = []
    upperhalf = []
    a = math.floor(math.sqrt(x))
    while a >= 1:
        if x % a == 0:
            lowerhalf.append(a)
        a -= 1
    for y in lowerhalf:
        if y != math.sqrt(x) and y != 1:
            upperhalf.append(int(x/y))
    combined = lowerhalf + upperhalf
    combined.sort()
    return sum(combined)

results = []

for a in range(2,10000):
    if factoring(factoring(a)) == a and a != factoring(a):
        results.append(a)
        print(a, factoring(a))

print(results)
print(sum(results))
    
