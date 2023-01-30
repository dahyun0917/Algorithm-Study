#BackJoon 2178 미로탐색
import sys
from collections import deque

def bfs(sx,sy,g):
    queue=deque()
    queue.append((sx,sy))
    while len(queue)!=0:
        x,y=queue.popleft()
        for i in range(4):
            if 0 <= x+dx[i] < N and 0<=y+dy[i]< M:
                if g[x+dx[i]][y+dy[i]] == 1:
                    g[x+dx[i]][y+dy[i]]= g[x][y]+1
                    queue.append((x+dx[i],y+dy[i]))
    
    
N,M=map(int,sys.stdin.readline().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int,str(sys.stdin.readline().strip()))))
dx=[1,-1,0,0] #상하좌우
dy=[0,0,1,-1] #상하좌우

bfs(0,0,graph)

print(graph[N-1][M-1])
