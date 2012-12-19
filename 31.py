def thcheck(ones, twos, fives, tens, twenties, fifties, hundreds):
    if ones + 2 * twos + 5 * fives + 10 * tens + 20 * twenties + 50 * fifties + 100 * hundreds == 200:
        return True
    else:
        return False

solutions = 2

for ones in xrange(0, 201):
    for twos in xrange(0, 101):
        for fives in xrange(0, 41):
            for tens in xrange(0, 21):
                for twenties in xrange(0, 11):
                    for fifties in xrange(0, 5):
                        for hundreds in xrange(0, 2):
                            if thcheck(ones, twos, fives, tens, twenties, fifties, hundreds) == True:
                                solutions += 1
                                print(solutions)
                                
