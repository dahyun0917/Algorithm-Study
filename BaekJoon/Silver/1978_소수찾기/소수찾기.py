#BackJoon 1978 소수찾기
import sys
import math

N=int(sys.stdin.readline())
n = list(map(int,sys.stdin.readline().split()))

count=0

for i in n:
    temp=True
    if i==1 : continue
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            temp=False
            break
    if temp : count+=1
    
print(count)
