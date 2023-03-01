#BackJoon 244444 알고리즘 수업 _ 너비 우선 탐색
import sys
from collections import deque
input=sys.stdin.readline
def bfs(s):
    queue=deque()
    queue.append(s)
    count=1  # 순서
    visited[s]=count
    while queue:
        q = queue.popleft()
        for g in sorted(graph[q]):
            if visited[g]==0:
                count+=1
                visited[g]=count
                queue.append(g)
N,M,R = map(int,input().split())
graph=[[] for _ in range(N+1)]
visited=[0 for _ in range(N+1)]
visited[0]=-1
for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
bfs(R)
for i in range(1,N+1):
    print(visited[i])
