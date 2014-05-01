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

nonsum = []

def test(x):
    for y in abundants:
        if y > x:
            return True
        if x - y in abundants:
            return False
    return True

for x in xrange(1, 28123):
    if test(x) == True:
        nonsum.append(x)
        print(x)

print(sum(nonsum))        


