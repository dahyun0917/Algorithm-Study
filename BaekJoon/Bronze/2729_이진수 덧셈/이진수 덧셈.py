#BackJoon 2729 이진수 덧셈
import sys

n= int(sys.stdin.readline())
result=[]
for _ in range(n):
    result.clear()
    a,b = list(map(str,sys.stdin.readline().split()))
    a_index=len(a)-1
    b_index=len(b)-1
    while a_index>=0 or b_index>=0:
        temp=0
        if a_index>=0: 
            temp+=int(a[a_index])
            a_index-=1
        if b_index>=0: 
            temp+=int(b[b_index])
            b_index-=1
        result.append(temp)
    for i in range(len(result)):
        if result[i]>1:
            if i==len(result)-1: result.append(result[i]//2)
            else: result[i+1]+=result[i]//2
            result[i]=result[i]%2
    result.reverse()
    true=False
    result_total=''
    for i in range(len(result)): 
        if result[i]==1 : true=True
        if true: result_total=result_total+str(result[i])
    if not true: print(0)
    else: print(result_total)
            
    
        
