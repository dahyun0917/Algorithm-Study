#BackJoon 10773 제로만들기 
import sys

n=int(sys.stdin.readline())
stack=[]
result=0

for _ in range(n):
    num = int(sys.stdin.readline())
    if(num==0):
        result-=stack.pop()
    else:
        stack.append(num)
        result+=num


print(result)         
