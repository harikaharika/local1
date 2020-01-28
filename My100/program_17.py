# 17. Write a program that computes the net amount of a bank account based a transaction log from
# console input. The transaction log format is shown as following:

d=0
w=0
l=[]
while True:
    x=input()
    if x:
        if x[0]=='D':
            dipct=x[2: ]
            d+=int(dipct)
        elif x[0]=='W':
            withdrw=x[2: ]
            w+=int(withdrw)
    else:
        break
transaction=d-w
print(transaction)