import math

solutions = 0

for x in range(1, 101):
    for y in range(1, x):
        if (math.factorial(x))/((math.factorial(y)) * (math.factorial(x-y))) > 1000000:
            solutions += 1

print(solutions)
