import math

def primechecker(x):
    if x < 0:
        return False
    for y in range(2, (math.floor(math.sqrt(x))) + 1):
        if x % y == 0:
            return False
    return True

currenttop = 0

for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        n = 0
        complete = False
        while complete != True:
            if primechecker((n ** 2) + (a * n) + b) == True:
                n += 1
            else:
                complete = True
                if n > currenttop:
                    currenttop = n
                    answers = [a, b]

print(answers)
                    
                
        
