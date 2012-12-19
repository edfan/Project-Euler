def decimal_to_binary(decimal):
    binaryresult = ''
    while decimal > 0:
        binaryresult = str(decimal % 2) + binaryresult
        decimal /= 2
    return int(binaryresult)

def palindrome(x):
    currentnum = []
    a = len(str(x)) - 1
    reversex = ''
    while a >= 0:
        currentnum.append(str(x)[a])
        a -= 1
    for y in currentnum:
        reversex += y
    if x == int(reversex):
        return True
    else:
        return False

answers = []

for x in xrange(1, 1000000):
    if palindrome(x) == True and palindrome(decimal_to_binary(x)) == True:
        answers.append(x)
        print(x)

print(answers)
print(sum(answers))
