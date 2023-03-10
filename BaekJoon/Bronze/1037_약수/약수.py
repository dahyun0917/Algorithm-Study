#BackJoon 1037 약수
import sys
N=int(sys.stdin.readline())
nlist=list(map(int,sys.stdin.readline().split()))
nlist.sort()
print(nlist[0]*nlist[-1])
