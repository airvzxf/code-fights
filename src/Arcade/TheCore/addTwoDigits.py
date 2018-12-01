def addTwoDigits(n):
    return sum(int(x) for x in str(n))


assert addTwoDigits(29) == 11
assert addTwoDigits(48) == 12
assert addTwoDigits(10) == 1
assert addTwoDigits(25) == 7
