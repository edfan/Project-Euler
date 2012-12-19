def pandigital(x):
    currentnum = []
    for y in str(x):
        currentnum.append(int(y))
    currentnum.sort()
    if currentnum == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return True
    else:
        return False

currentmax = 0

for x in range(10, 34):
    concenated = int(str(x) + str(2 * x) + str(3 * x) + str(4 *x))
    if pandigital(concenated) == True and concenated > currentmax:
        currentmax = concenated
        print(x)

for x in range(100, 334):
    concenated = int(str(x) + str(2 * x) + str(3 * x))
    if pandigital(concenated) == True and concenated > currentmax:
        currentmax = concenated
        print(x)

for x in range(5000, 10000):
    concenated = int(str(x) + str(2 * x))
    if pandigital(concenated) == True and concenated > currentmax:
        currentmax = concenated
        print(x)

print(currentmax)
