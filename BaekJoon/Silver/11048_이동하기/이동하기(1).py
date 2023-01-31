#BackJoon 11048 이동하기
from collections import deque
import sys

def bfs(sx,sy,g):
    queue=deque()
    queue.append((sx,sy))
    result[0][0]=g[0][0]
    while len(queue)!=0 :
        x,y = queue.popleft()
        for i in range(3):
            if 0<=x+dx[i]<N and 0<=y+dy[i]<M:
                if result[x+dx[i]][y+dy[i]]!=0 and result[x+dx[i]][y+dy[i]]< g[x+dx[i]][y+dy[i]]+result[x][y]:
                    result[x+dx[i]][y+dy[i]]= g[x+dx[i]][y+dy[i]]+result[x][y]
                    queue.append((x+dx[i],y+dy[i]))
                elif result[x+dx[i]][y+dy[i]]==0:
                    result[x+dx[i]][y+dy[i]]= g[x+dx[i]][y+dy[i]]+result[x][y] 
                    queue.append((x+dx[i],y+dy[i]))
        
        
    
N,M = map(int,sys.stdin.readline().split())
graph=[]
result=[[0 for _ in range(M)] for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))

dx = [1,0,1]
dy = [0,1,1]

bfs(0,0,graph)
print(result[N-1][M-1])
