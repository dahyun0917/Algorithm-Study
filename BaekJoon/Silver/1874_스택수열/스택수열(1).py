#BackJoon 1874 스택수열
import sys

n= int(sys.stdin.readline())
stack=[]
number=[]
result=[]

for _ in range(n):
    number.append(int(sys.stdin.readline()))
    if len(number)==1: 
        for i in range(1,number[0]+1):
            stack.append(i)
            result.append('+')
count=len(stack)
while len(number)!=0:
    if len(stack)==0:
       while count!=number[0] :
            count+=1
            stack.append(count)
            result.append('+') 
    if stack[-1]==number[0]: 
        number.pop(0)
        stack.pop()
        result.append('-')
    elif stack[-1] < number[0] :
        while count!=number[0] :
            count+=1
            stack.append(count)
            result.append('+')
    else:
        print('NO')
        break

if len(number)==0:
    for i in result: print(i)
