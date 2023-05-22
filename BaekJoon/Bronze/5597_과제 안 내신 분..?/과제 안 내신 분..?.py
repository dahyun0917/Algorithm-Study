nlist=[i for i in range(1,31)]
for i in range(28):
    temp=int(input())
    nlist.pop(nlist.index(temp))
for n in nlist:
    print(n)
