# 10. Write a program that accepts a sequence of whitespace separated words as input
# and prints the words after removing all duplicate words and
# sorting them alphanumerically.

s=input()
words=s.split()
print(" ".join(sorted(set(words))))
