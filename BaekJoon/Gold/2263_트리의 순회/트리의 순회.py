#BackJoon 2263 트리의 순회
import sys
sys.setrecursionlimit(10**8)

def preOrder(in_start,in_end,post_start,post_end):
    if in_start>in_end or post_start > post_end :
        return
    root=postOrder[post_end]
    size=pos[root]-in_start
    ans.append(root)
    
    preOrder(in_start, pos[root]-1 , post_start, post_start+size-1)
    preOrder(pos[root]+1, in_end, post_start+size , post_end-1 )
    
    
n=int(sys.stdin.readline())
inOrder=[-1]+list(map(int,sys.stdin.readline().split()))
postOrder=[-1]+list(map(int,sys.stdin.readline().split()))

pos = [-1]*(n+1) 
for i in range(n+1):
    pos[inOrder[i]] = i
ans = []


preOrder(1,n,1,n)
print(*ans)
