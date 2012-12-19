import math

def factorial(x):
    currentnum = []
    currentfactorials = []
    for a in str(x):
        currentnum.append(int(a))
    for b in currentnum:
        currentfactorials.append(math.factorial(b))
    if sum(currentfactorials) == x and x != 1 and x != 2:
        return True
    else:
        return False

results = []

for num in xrange(1,1000000):
    if factorial(num) == True:
        results.append(num)
        print(num)

print(results)
print(sum(results))
