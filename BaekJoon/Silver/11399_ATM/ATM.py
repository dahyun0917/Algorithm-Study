#BackJoon 11399 ATM
import sys

n=int(input())
time=list(map(int,input().split()))
temp=0
result=0
time.sort()

for t in time:
    temp+=t
    result+=temp
print(result)
