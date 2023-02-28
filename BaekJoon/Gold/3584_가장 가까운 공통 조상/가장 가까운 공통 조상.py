#BackJoon 3584 가장 가까운 공통 조상
import sys
import math
from collections import deque
input=sys.stdin.readline
def LCA(a,b):
    queue=deque() # queue보다 조금 더 빠른 것 같아서 deque 사용
    length=math.inf
    sca=0
    aDic={}
    bDic={}
    
    queue.append((a,"aDic",0))
    aDic[a]=0
    queue.append((b,"bDic",0))
    bDic[b]=0
    
    while queue :
        v = queue.popleft()
        if v[2] > length : break
        g= fromVertex[v[0]]
        if v[0]==-1 : continue
        if v[1] == "aDic":
            if not (g in aDic):
                aDic[g]=v[2]+1
                queue.append((g,"aDic",v[2]+1))
            if g in bDic: 
                if length> aDic[g]+bDic[g] : 
                    length=aDic[g]+bDic[g]
                    sca=g
        elif v[1] == "bDic":
            if not (g in bDic):
                bDic[g]=v[2]+1
                queue.append((g,"bDic",v[2]+1))
            if g in aDic :
                if length > aDic[g]+bDic[g] :
                    length= aDic[g]+bDic[g]
                    sca=g
    return sca
            
for i in range(int(input())):   
    N=int(input())
    fromVertex = [-1 for i in range(N+1)]
    for i in range(N-1):
        a,b = map(int, input().split())
        fromVertex[b]=a
    a,b = map(int,input().split())
    print(LCA(a,b))
        
