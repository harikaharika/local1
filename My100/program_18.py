# 18. A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12

import string
x=input()
values=x.split(',')
l='$#@'
lis=[]
for s in values:
    d={}
    if len(s)>=6 and len(s)<=12:
        d[1]=1
        for i in s:
            if i in string.ascii_lowercase:
                d[2]=1
            if i in string.ascii_uppercase:
                d[3]=1
            if i in string.digits:
                d[4]=1
            if i in l:
                d[5]=1
            else:
                pass
        sum=0
        for i in d.values():
            sum+=1
        if sum==5:
            lis.append(s)
print(lis)

