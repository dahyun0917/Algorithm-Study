#BackJoon 1546 평균
import sys
n=int(sys.stdin.readline())
nlist=list(map(int,sys.stdin.readline().split()))
M=max(nlist)

for i in range(n):
    nlist[i]=(nlist[i]/M)*100

print(sum(nlist)/n)
