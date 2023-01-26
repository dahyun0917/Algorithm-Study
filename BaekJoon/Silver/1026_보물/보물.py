#BackJoon 1026 보물
import sys

n=int(sys.stdin.readline())

a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))

a= sorted(a)
b= sorted(b)
result=0

for i in range(len(b)):
    result+=a[i]*b[len(b)-1-i]
 
print(result)
    
