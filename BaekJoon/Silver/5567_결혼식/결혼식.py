#BaekJoon 5567 결혼식
import sys
input = sys.stdin.readline
def bfs():
    count=0
    queue=[(1,0)]
    visited[1]=True
    while queue:
        n,num = queue.pop(0)
        if num>1 : return count
        for f in friend[n]:
            if not visited[f]:
                visited[f]=True
                count+=1
                queue.append((f,num+1))
    return count
n = int(input())
m = int(input())
friend = [[] for _ in range(n+1)]
visited=[False for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)
print(bfs())
