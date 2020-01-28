f=open("x.py")
try:
    a=5
    b=int(input('enter:'))
    c=a/b
except:
    if b==0:
        print("your given values is zero" )
else:
    print(c)
finally:
    f.close()
