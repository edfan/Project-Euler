odd = ['1', '3', '5', '7', '9']

def reversible(x):
    reversex = ''
    for y in str(x):
        reversex = y + reversex
    combined = x + int(reversex)
    if str(reversex)[0] == '0':
        return False
    for z in str(combined):
        if z not in odd:
            return False
    return True

reversibles = 0

for x in xrange(1, 1000000000):
    if reversible(x) == True:
        reversibles += 1
        print(x)

print(reversibles)
