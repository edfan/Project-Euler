test = []
for x in range(100,1000):
    for y in range(100,1000):
        test.append(x*y)

test.sort()

palindromes = []

for a in test:
    if len(str(a)) == 6:
        reverse = ''
        reverse += str(a)[5]
        reverse += str(a)[4]
        reverse += str(a)[3]
        reverse += str(a)[2]
        reverse += str(a)[1]
        reverse += str(a)[0]
        if int(reverse) == a:
            palindromes.append(a)

print(palindromes)


