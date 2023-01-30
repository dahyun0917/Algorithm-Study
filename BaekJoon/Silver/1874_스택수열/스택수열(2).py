#BackJoon 1874 스택수열
import sys

n= int(sys.stdin.readline())

stack=[]
result=[]
count=1

for i in range(n):
    num=int(sys.stdin.readline())
    while count<=num:
        stack.append(count)
        result.append('+')
        count+=1
    if stack[-1]==num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        break
if i==n-1:
    for r in result: print(r)
