#BackJoon 2357 최솟값과 최댓값
import sys
import math
sys.setrecursionlimit(10**8)
input=sys.stdin.readline
N,M=map(int,input().split())
h=int(math.ceil(math.log2(N)))
t_size=1<<(h+1)
tree=[0]*(t_size)
min_tree=[0]*(t_size)
graph=[int(input()) for _ in range(N)]

def init_max(start,end,index):
    if start==end :
        tree[index]=graph[start]
        return tree[index]
    mid=(start+end)//2
    a=init_max(start,mid,index*2)
    b=init_max(mid+1,end,index*2+1)
    tree[index]=max(a,b)
    return tree[index]
def init_min(start,end,index):
    if start==end :
        min_tree[index]=graph[start]
        return min_tree[index]
    mid=(start+end)//2
    a=init_min(start,mid,index*2)
    b=init_min(mid+1,end,index*2+1)
    min_tree[index]=min(a,b) 
    return min_tree[index]

# left : 구간 a , right : 구간 b
def find_max(start,end,left,right,index):
    if left > end or right < start: return -1
    if left <= start and right >= end: return tree[index]
    mid=(start+end)//2 
    a=find_max(start,mid,left,right,index*2)
    b=find_max(mid+1,end,left,right,index*2+1)
    return max(a,b)

def find_min(start,end,left,right,index):
    if left > end or right < start: return 1000000001
    if left <= start and right >= end: return min_tree[index]
    mid=(start+end)//2 
    a=find_min(start,mid,left,right,index*2)
    b=find_min(mid+1,end,left,right,index*2+1)
    return min(a,b)

init_max(0,N-1,1)
init_min(0,N-1,1)
for _ in range(M):
    a,b=map(int,input().split())
    print(find_min(0,N-1,a-1,b-1,1),find_max(0,N-1,a-1,b-1,1))
