# is_leap returns True for years divisible by 400, False for other century years, and
# True for the remaining years divisible by 4.

def is_leap(year):
    leap = False

    if (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
        return True
    elif (year % 4 == 0) and (year % 100 == 0):
        return False
    elif year % 4 == 0:
        return True
    else:
        return leap

year = int(input())
print(is_leap(year))