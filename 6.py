x = 100
numbers = []
result = []

while x > 0:
    numbers.append(x)
    x -= 1

numbers.sort()

for n in numbers:
    result.append(n ** 2)

result2 = sum(numbers) ** 2
result3 = sum(result)

print(result2)
print(result3)
print (result2 - result3)
