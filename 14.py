top = 999999
numbers = []
while top > 300000:
    numbers.append(top)
    top -= 1

current = 0
result = 0

for n in numbers:
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            current += 1
        else:
            n = n * 3 + 1
            current += 1
    if current == 524:
        result = n
    current = 0

print(result)
