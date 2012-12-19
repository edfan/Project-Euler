numbers = []
result = []
top = 999

while top > 0:
    numbers.append(top)
    top -= 1

numbers.sort()

for n in numbers:
    if n % 3 == 0:
        result.append(n)
    elif n % 5 == 0:
        result.append(n)

print (sum(result))
        
