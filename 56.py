currentmax = 0

for x in range(1, 100):
    for y in range(1, 100):
        current = x ** y
        currentlist = []
        for z in str(current):
            currentlist.append(int(z))
        if sum(currentlist) > currentmax:
            currentmax = sum(currentlist)
            print(currentmax)

print(currentmax)
