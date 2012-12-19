totalsum = 0
results = []

for x in range(1, 100):
    for y in range(100, 10000):
        z = x * y
        currentlist = []
        for a in str(x):
            currentlist.append(int(a))
        for a in str(y):
            currentlist.append(int(a))
        for a in str(z):
            currentlist.append(int(a))
        currentlist.sort()
        if currentlist == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if z not in results:
                results.append(z)
                print(x, y, z)
                totalsum += z

print(totalsum)
            
