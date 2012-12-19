def chain(x):
    while x != 1 and x != 89:
        nextx = 0
        for a in str(x):
            nextx += int(a) ** 2
        x = nextx
    if x == 89:
        return True
    else:
        return False

solutions = 0

for x in xrange(1, 10000000):
    if chain(x) == True:
        solutions += 1
