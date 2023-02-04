#BackJoon 13023 ABCDE
import sys

def dfs(graph,v,visited,count,c):
    result=False
    visited[v]=True
    count[v]=c+1
    if count[v]==5 : return True
    
    for i in graph[v]:
        if visited[i]==False: 
            if dfs(graph,i,visited,count,count[v]): result=True
    visited[v]=False
    count[v]=0
    return result
        
    
N,M=map(int,sys.stdin.readline().split())
visited=[]
count=[]
graph=[[] for i in range(N)]
result=0

for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    visited.clear()
    count.clear()
    visited=[False]*(N+1)
    count=[0]*(N+1)
    if dfs(graph,i,visited,count,0): 
        result=1
        break
print(result)
