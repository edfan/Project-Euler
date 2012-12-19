nterm = 50

positions = []
result = [1, 2]
result2 = []
while nterm > 2:
    positions.append(nterm)
    nterm -= 1
positions.sort()
for n in positions:
    current = result[n-2] + result[n-3]
    result.append(current)

for n in result:
    if n % 2 == 0:
        if n < 4000000:
            result2.append(n)

print(sum(result2))
