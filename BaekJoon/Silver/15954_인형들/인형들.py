#BaekJoon 15954 인형들
#pypy로 돌림
import sys
import math
input = sys.stdin.readline
N,K = map(int,input().split())
nlist = list(map(int,input().split()))
result = float('inf')

for i1 in range(N): #시작점
    for i2 in range(i1+K-1,N): # 끝 점
        vsum=0
        mean = sum(nlist[i1:i2+1])/(i2-i1+1)
        for j in range(i1,i2+1):vsum+= (nlist[j]-mean)**2
        # result=min(result,(vsum/(i2-i1+1)))
        result=min(result,math.sqrt((vsum/(i2-i1+1))))
# print(round(result**0.5,11))
print(round(result,11))
