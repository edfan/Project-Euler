namefile = open('names.txt')
namestring = namefile.read()
namefile.close()
names = []

currentname = ''

for char in namestring:
    if char == '"' or char == ',':
        if currentname != '':
            names.append(currentname)
            currentname = ''
    else:
        currentname = currentname + char

names.sort()

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
total = 0

for name in names:
    currentnamescore = 0
    for char in name:
        currentnamescore += letters.index(char) + 1
    total += currentnamescore * (names.index(name) + 1)

print(total)
