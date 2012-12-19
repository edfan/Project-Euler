import math

def power(x):
    currentnum = []
    fifth = []
    for a in str(x):
        currentnum.append(int(a))
    for b in currentnum:
        fifth.append(math.pow(b,5))
    if sum(fifth) == x and x != 1:
        return True
    else:
        return False

results = []

for y in xrange(1,1000000):
    if power(y) == True:
        results.append(y)
        print(y)

print(results)
print(sum(results))
        
                     
