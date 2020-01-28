# 22. Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.

import collections
s=input()
x=s.split()
m=collections.Counter(x)
print(m)

