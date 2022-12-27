#Backjoon 1260
#[dfs/bfs] DFS와 BFS
from collections import deque

def dfs(v,visited):
   visited[v]=True
   print(v+1,end=' ')
   
   for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)

def bfs(start):
    visited=[0]*n
    queue=deque()
    queue.append(start)
    visited[start]=1
    
    while(queue):
        v=queue.popleft()
        print(v+1,end=' ')
        for i in graph[v]:
            if(visited[i]==0):
                visited[i]=1
                queue.append(i)
                
n,m,start=map(int,input().split())
visited_dfs=[False]*n
graph=[[] for i in range(n)]

#연결된 노드 입력받기
for i in range(m):
    x,y=map(lambda a: int(a)-1,input().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()

dfs(start-1,visited_dfs)
print()
bfs(start-1)
