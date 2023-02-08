#BackJoon 2581 소수
import sys
import math

M=int(sys.stdin.readline())
N=int(sys.stdin.readline())

graph=[True for i in range(N+1)]
graph[0]=False
graph[1]=False
for i in range(2,int(math.sqrt(N))+1):
    if graph[i]:
        j=2
        while i*j <= N:
            graph[i*j] = False
            j+=1

decimal=[]
for i in range(M,N+1):
    if graph[i] : decimal.append(i)

if len(decimal)==0 : print(-1)
else:
    print(sum(decimal))
    print(min(decimal))
