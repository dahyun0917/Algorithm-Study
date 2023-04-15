#BaekJoon 1427 소트인사이드
nlist=list(map(str,input()))
for n in sorted(nlist,reverse=True):
    print(n,end='')
