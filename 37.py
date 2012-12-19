from math import sqrt, floor

def prime(x):
    if x == 1:
        return False
    for y in range(2, int(floor(sqrt(x))+1)):
        if x % y == 0:
            return False
    return True

def left_to_right(x):
    x = str(x)
    while len(x) > 1:
        x = x[1:]
        if prime(int(x)) == False:
            return False
    return True

def right_to_left(x):
    x = str(x)
    while len(x) > 1:
        x = x[0:(len(x)-1)]
        if prime(int(x)) == False:
            return False
    return True

solutions = []

for x in range(10, 1000000):
    if prime(x) == True:
        if left_to_right(x) == True and right_to_left(x) == True:
            solutions.append(x)

print(solutions)
print(sum(solutions))
