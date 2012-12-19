triangle = []
pentagonal = []
hexagonal = []

for x in range(1, 100000):
    triangle.append((x*(x+1))/2)
    pentagonal.append((x*(3*x-1))/2)
    hexagonal.append(x*(2*x-1))

tph = []
tphpositions = []

for y in triangle:
    if y in pentagonal:
        if y in hexagonal:
            tph.append(y)
            tphpositions.append(triangle.index(y))
            print(y)

print(tph)
print(tphpositions)

