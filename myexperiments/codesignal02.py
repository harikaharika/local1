# 2.Given a year, return the century it is in.
# The first century spans from the year 1 up to and including the year 100,
# the second - from the year 101 up to and including the year 200, etc.


def centuryFromYear(year):
    x=year/100
    y=year%100
    if y==0:
        return int(x)
    else:
        return int(x)+1
centuryFromYear(1905)