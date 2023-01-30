#BackJoon 2740 행렬곱셈
import sys

N,M = map(int,sys.stdin.readline().split())
A=[]
for _ in range(N):
    A.append(list(map(int,sys.stdin.readline().split())))
M,K = map(int,sys.stdin.readline().split())
B=[]
for _ in range(M):
    B.append(list(map(int,sys.stdin.readline().split())))

for i in range(N):
    for j in range(K):
        sum=0
        for k in range(M):
            sum+=A[i][k]*B[k][j]
        print(sum,end=' ')
    print()
