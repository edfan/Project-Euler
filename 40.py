numberstring = ''

for x in range(1, 1000000):
    numberstring += str(x)

print(numberstring)

print(int(str(x)[0]) * int(str(x)[9]) * int(str(x)[99]) * int(str(x)[999]) * int(str(x)[9999]) * int(str(x)[99999]) * int(str(x)[999999]))
