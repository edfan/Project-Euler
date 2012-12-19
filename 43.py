def pandigital(x):
    listx = []
    for a in str(x):
        listx.append(int(a))
    listx.sort()
    if listx == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return True
    else:
        return False

def divisible(x):
    listx = []
    for a in str(x):
        listx.append(a)
    if int(listx[1] + listx[2] + listx[3]) % 2 != 0:
        return False
    elif int(listx[2] + listx[3] + listx[4]) % 3 != 0:
        return False
    elif int(listx[3] + listx[4] + listx[5]) % 5 != 0:
        return False
    elif int(listx[4] + listx[5] + listx[6]) % 7 != 0:
        return False
    elif int(listx[5] + listx[6] + listx[7]) % 11 != 0:
        return False
    elif int(listx[6] + listx[7] + listx[8]) % 13 != 0:
        return False
    elif int(listx[7] + listx[8] + listx[9]) % 17 != 0:
        return False
    else:
        return True

assert pandigital(1406357289) == True
assert divisible(1406357289) == True

solutions = []

for x in xrange(1234567890, 9876543210):
    if int(str(x)[3]) % 2 == 0:
        if pandigital(x) == True:
            if divisible(x) == True:
                solutions.append(x)
                print(x)
