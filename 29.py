import math
results = []

for a in range(2,101):
    for b in range(2,101):
        if a ** b not in results:
            results.append(a ** b)

print(len(results))
