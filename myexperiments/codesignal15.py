def addBorder(picture):
    a=[]
    b= ""
    for i in range(0, len(picture[0]) + 2):
        b+= "*"
    a.append(b)
    for i in range(0, len(picture)):
        a.append("*" + picture[i] + "*")

    a.append(b)

    return a
res=addBorder(picture = ["abc","ded"])
print(res)