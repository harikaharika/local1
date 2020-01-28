# 4. Write a program which accepts a sequence of comma-separated numbers from
# console and generate a list and a tuple which contains every number.

x=input()
list=x.split(",")
tuple=tuple(list)
print('List:',list)
print('Tuple:',tuple)