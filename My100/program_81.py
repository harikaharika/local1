# 81. Please write a program to compress and decompress the string
# "hello world!hello world!hello world!hello world!".

import zlib
s = "hello world!hello world!hello world!hello world!"
comp = zlib.compress(s,2)
print(comp)
decomp = zlib.decompress(comp)
print(decomp)