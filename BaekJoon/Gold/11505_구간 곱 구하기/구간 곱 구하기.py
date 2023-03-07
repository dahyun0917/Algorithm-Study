#BackJoon 11505 구간 곱 구하기
#https://www.acmicpc.net/board/view/102955
import sys
sys.setrecursionlimit(10**8)

def init(start,end,index):
    if start==end : 
        tree[index]=arr[start]
        return tree[index]%1000000007
    mid=(start+end)//2
    tree[index]=init(start,mid,index*2)*init(mid+1,end,index*2+1)
    return tree[index]%1000000007

def inter_pro(start,end,index,left,right):
    if left > end or right < start: return 1
    if start>=left and end<=right :
        return tree[index]
    mid=(start+end)//2
    return inter_pro(start,mid,index*2,left,right)*inter_pro(mid+1,end,index*2+1,left,right)%1000000007

def update(start,end,node,index,dif):
    if index<start or index>end: return 
    if start==end:
        tree[node]=dif
        return 
    mid=(start+end)//2
    update(start,mid,node*2,index,dif)
    update(mid+1,end,node*2+1,index,dif)
    tree[node]=tree[node*2]*tree[node*2+1]
    tree[node]%=1000000007
    
N,M,K = map(int,sys.stdin.readline().split())
arr=list(int(sys.stdin.readline()) for _ in range(N))
tree=[0]*(4*N+1)
init(0,len(arr)-1,1)
for _ in range(M+K):
    a,b,c = map(int,sys.stdin.readline().split())
    if a==1 : update(0,len(arr)-1,1,b-1,c)
    elif a==2 : print(int(inter_pro(0,len(arr)-1,1,b-1,c-1)))
