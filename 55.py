def palindrome(x):
    reversex = ''
    a = len(str(x)) - 1
    while a >= 0:
        reversex += str(x)[a]
        a -= 1
    return int(reversex)

def lycherl(x):
    iterations = 0
    currentnum = x + palindrome(x)
    while iterations <= 50:
        if palindrome(currentnum) == currentnum:
            return False
        else:
            currentnum += palindrome(currentnum)
            iterations += 1
    return True

lycherlnums = []

for x in range(1, 10001):
    if lycherl(x) == True:
        lycherlnums.append(x)

print(lycherlnums)
print(len(lycherlnums))
