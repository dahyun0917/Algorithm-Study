#BackJoon 1789 수들의 합
import sys

S=int(sys.stdin.readline())
n=1
count=0

while True:
    if(S<n): break
    S-=n
    n+=1
    count+=1
    
print(count)
