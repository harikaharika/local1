# def cfy(year):
#     if year >= 1901 and year <= 1999:
#         a = (year / 100) + 1
#         return "centuryFromYear(year) = " + a
#     elif year >= 1601 and year <= 1700:
#         b = year / 100
#         return "centuryFromYear(year) = " + b
#     else:
#         pass
#
#
# res = cfy(1905)
# print(int(res))


def checkPalindrome(inputString):
    return inputString==inputString[::-1]
res=checkPalindrome("121")
print(res)