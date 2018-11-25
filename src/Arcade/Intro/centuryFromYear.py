from math import ceil


def centuryFromYear(year):
    decimal_year = year / 100
    return ceil(decimal_year)


print(centuryFromYear(1905), 20)
print(centuryFromYear(1700), 17)
print(centuryFromYear(1988), 20)
print(centuryFromYear(200), 2)
print(centuryFromYear(374), 4)
print(centuryFromYear(45), 1)
