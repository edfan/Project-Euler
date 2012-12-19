import math

def abundantfactor(x):
    lowerhalf = []
    upperhalf = []
    a = math.floor(math.sqrt(x))
    while a >= 1:
        if x % a == 0:
            lowerhalf.append(a)
        a -= 1
    for y in lowerhalf:
        if y != 1 and y != math.sqrt(x):
            upperhalf.append(int(x/y))
    factors = upperhalf + lowerhalf
    factors.sort()
    if sum(factors) > x:
        return True
    else:
        return False

abundants = []

for x in range(1, 28123):
    if abundantfactor(x) == True:
        abundants.append(x)

sums = []

for x in abundants:
    for y in abundants:
        if x + y <= 28123 and x + y not in sums:
            sums.append(x+y)
            print(x+y)

nonsum = []

for x in range(1,28123):
    if x not in sums:
        nonsum.append(x)
        print(x)

print(sum(nonsum))        


