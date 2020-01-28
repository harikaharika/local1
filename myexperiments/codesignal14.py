def alternatingSums(a):
    return [sum(a[::2]), sum(a[1::2])]
res=alternatingSums([50, 60, 60, 45, 70])
print(res)