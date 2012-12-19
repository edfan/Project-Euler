answers = []
correct = False

for x in range(1, 1000000):
    if correct == False:
        digits = []
        digits2 = []
        digits3 = []
        digits4 = []
        digits5 = []
        digits6 = []
        for y in range(len(str(x))):
            digits.append(str(x)[y])
        for y in range(len(str(2*x))):
            digits2.append(str(2*x)[y])
        for y in range(len(str(3*x))):
            digits3.append(str(3*x)[y])
        for y in range(len(str(4*x))):
            digits4.append(str(4*x)[y])
        for y in range(len(str(5*x))):
            digits5.append(str(5*x)[y])
        for y in range(len(str(6*x))):
            digits6.append(str(6*x)[y])
        digits.sort()
        digits2.sort()
        digits3.sort()
        digits4.sort()
        digits5.sort()
        digits6.sort()
        if digits == digits2 and digits == digits3 and digits == digits4 and digits == digits5 and digits == digits6:
            print(x)
            correct = True
    
           
