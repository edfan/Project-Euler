solutions = 0

for x in range(1, 10):
    for y in range(1, 50):
        if len(str(x**y)) == y:
            solutions += 1
            print(x**y)
        
