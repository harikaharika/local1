# def mygen(x,y):
#     while x<=y:
#         yield x
#         x+=1
# g=mygen(1,12)
# for i in g:
#     print(i)

# g1=iter(g)
# print(next(g1))

#
# def mygen(x,y):
#     while x<=y:
#         yield x
#         x+=1
# g=mygen(1,12)
# for i in g:
#     print(i)


def mygen(x,y):
    while x<=y:
        yield x
        x+=1
g=mygen(5,10)
for i in g:
    print(i)

