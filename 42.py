wordfile = open('words.txt')
wordstring = wordfile.read()
wordfile.close()
words = []

currentword = ''

for char in wordstring:
    if char == '"' or char == ',':
        if currentword != '':
            words.append(currentword)
            currentword = ''
    else:
        currentword = currentword + char

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
solutions = 0

triangle = []
for x in range(1, 100):
    triangle.append((x * (x+1)) / 2)

for word in words:
    currentwordscore = 0
    for char in word:
        currentwordscore += letters.index(char) + 1
    if currentwordscore in triangle:
        solutions += 1

print(solutions)
