# 98. Write a program to solve a classic ancient Chinese puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm.
# How many rabbits and how many chickens do we have?

nheads=35
nlegs=94
for i in range(nheads+1):
    j=nheads-i
    if 2*i+4*j==nlegs:
        print(i,j)



























