#BaekJoon 24479 알고리즘 수업 - 깊이 우선 탐색
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
def dfs(start):
    global cnt
    visited[start]=True
    result[start]=cnt
    cnt+=1
    for g in sorted(graph[start]):
        if not visited[g]:
            dfs(g)
N,M,R = map(int,input().split())
graph=[[] for _ in range(N+1)]
visited=[False for _ in range(N+1)]
result=[0 for _ in range(N+1)]
cnt=1
for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(R)
for r in result[1:]:
    print(r)
