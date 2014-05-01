day = 2
year = 1
month = 1
result = 0

while year < 500:
    if month == 1:
        if day % 7 == 0:
            result += 1
        day += 31
        month = 2
    if month == 2:
        if day % 7 == 0:
            result += 1
        if year % 4 == 0:
            day += 29
        elif year % 4 != 0:
            day += 28
        month = 3
    if month == 3:
        if day % 7 == 0:
            result += 1
        if day % 7 == 5:
            print year + 1900
        day += 31
        month = 4
    if month == 4:
        if day % 7 == 0:
            result += 1
        day += 30
        month = 5
    if month == 5:
        if day % 7 == 0:
            result += 1
        day += 31
        month = 6
    if month == 6:
        if day % 7 == 0:
            result += 1
        day += 30
        month = 7
    if month == 7:
        if day % 7 == 0:
            result += 1
        day += 31
        month = 8
    if month == 8:
        if day % 7 == 0:
            result += 1
        day += 31
        month = 9
    if month == 9:
        if day % 7 == 0:
            result += 1
        day += 30
        month = 10
    if month == 10:
        if day % 7 == 0:
            result += 1
        day += 31
        month = 11
    if month == 11:
        if day % 7 == 0:
            result += 1
        day += 30
        month = 12
    if month == 12:
        if day % 7 == 0:
            result += 1
        day += 31
        month = 1
        year += 1

print (result)
