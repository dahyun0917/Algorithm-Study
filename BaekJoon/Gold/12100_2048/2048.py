#BaekJoon 12100 2048
import sys
from collections import deque
def move(new,x,y,dx,dy,now):
    while 0<=x+dx<N and 0<=y+dy<N :
        if new[x+dx][y+dy]==0: 
            x,y=x+dx,y+dy
        elif new[x+dx][y+dy]==now:
            x,y=x+dx,y+dy
            break
    return x,y
def up(g,m):
    new=[[0 for _ in range(N)] for _ in range(N)]
    lock=[[0 for _ in range(N)] for _ in range(N)]  # 합쳐졌었는지 확인
    maxN=m
    for i in range(N):
        for j in range(N):
            # x,y = 0,j # 상
            x,y = move(new,i,j,-1,0,g[i][j])
            if new[x][y]==0 : 
                new[x][y]=g[i][j]  # 해당 노드에 아무 값도 없을 때
                maxN=max(maxN,new[x][y])
            else:  # 해당 노드에 값이 있을 경우
                if new[x][y]==g[i][j] and lock[x][y]!=1:  # 만약 같은 값일 경우
                    new[x][y]=new[x][y]*2  # 두배로 바꿔줌
                    lock[x][y]=1
                    maxN=max(maxN,new[x][y])
                else: # 현재 계산 된 값의 이동거리가 더 클 때
                    k=1
                    while 0<=x+k<N :
                        if new[x+k][y]==0 :  # 0 일때
                            new[x+k][y] = g[i][j]
                            maxN=max(maxN,new[x+k][y])
                            break
                        k+=1
    return new, maxN
def down(g,m):
    new=[[0 for _ in range(N)] for _ in range(N)]
    lock=[[0 for _ in range(N)] for _ in range(N)]  # 합쳐졌었는지 확인
    maxN=m
    for i in range(N-1,-1,-1):
        for j in range(N):
            # x,y= N-1,j # 하
            x,y = move(new,i,j,1,0,g[i][j])
            if new[x][y]==0: 
                new[x][y]=g[i][j]  # 해당 노드에 아무 값도 없을 때
                maxN=max(maxN,new[x][y])
            else:  # 해당 노드에 값이 있을 경우
                if new[x][y]==g[i][j]and lock[x][y]!=1:  # 만약 같은 값일 경우
                    new[x][y]=new[x][y]*2  # 두배로 바꿔줌
                    lock[x][y]=1
                    maxN=max(maxN,new[x][y])
                else: # 현재 계산 된 값의 이동거리가 더 클 때
                    k=1
                    while 0<=x-k<N :
                        if new[x-k][y]==0 :  # 0 일때
                            new[x-k][y] = g[i][j]
                            maxN=max(maxN,new[x-k][y])
                            break
                        k+=1
    return new, maxN
def left(g,m):
    new=[[0 for _ in range(N)] for _ in range(N)]
    lock=[[0 for _ in range(N)] for _ in range(N)]  # 합쳐졌었는지 확인
    maxN=m
    for j in range(N):
        for i in range(N):
            # x,y =i,0 # 좌
            x,y = move(new,i,j,0,-1,g[i][j])
            if new[x][y]==0 and new[x][y]==0: 
                new[x][y]=g[i][j] # 해당 노드에 아무 값도 없을 때
                maxN=max(maxN,new[x][y])
            else:  # 해당 노드에 값이 있을 경우
                if new[x][y]==g[i][j] and lock[x][y]!=1:  # 만약 같은 값일 경우
                    new[x][y]=new[x][y]*2  # 두배로 바꿔줌
                    lock[x][y]=1
                    maxN=max(maxN,new[x][y])
                else: # 현재 계산 된 값의 이동거리가 더 클 때
                    k=1
                    while 0<=y+k<N :
                        if new[x][y+k]==0 :  # 0 일때
                            new[x][y+k] = g[i][j]
                            maxN=max(maxN,new[x][y+k])
                            break
                        k+=1
    return new, maxN
def right(g,m):
    new=[[0 for _ in range(N)] for _ in range(N)]
    lock=[[0 for _ in range(N)] for _ in range(N)]  # 합쳐졌었는지 확인
    maxN=m
    for j in range(N-1,-1,-1):  # 가로
        for i in range(N):  # 세로 
            # x,y =i,N-1 # 우
            x,y = move(new,i,j,0,1,g[i][j])
            if new[x][y]==0 and new[x][y]==0: 
                new[x][y]=g[i][j]  # 해당 노드에 아무 값도 없을 때
                maxN=max(maxN,new[x][y])
            else:  # 해당 노드에 값이 있을 경우
                if new[x][y]==g[i][j] and lock[x][y]!=1:  # 만약 같은 값일 경우
                    new[x][y]=new[x][y]*2  # 두배로 바꿔줌
                    lock[x][y]=1
                    maxN=max(maxN,new[x][y])
                else:  # 현재 계산 된 값의 이동거리가 더 클 때
                    k=1
                    while 0<=y-k<N :
                        if new[x][y-k]==0 :  # 0 일때
                            new[x][y-k] = g[i][j]
                            maxN=max(maxN,new[x][y-k])
                            break
                        k+=1
    return new, maxN
    
def bfs():
    queue=deque()
    queue.append(([]+graph,0,2))
    result_max=2
    while queue:
        g,depth,maxN=queue.popleft()
        if depth==6: return result_max
        if depth<=5 : result_max=max(result_max,maxN)
				new,maxN_re = up(g,maxN)
        queue.append((new,depth+1,maxN_re))
        new,maxN_re = down(g,maxN)
        queue.append((new,depth+1,maxN_re))
        new,maxN_re = left(g,maxN)
        queue.append((new,depth+1,maxN_re))
        new,maxN_re = right(g,maxN)
        queue.append((new,depth+1,maxN_re))
                
    
    
N=int(sys.stdin.readline())
graph=[]
dx=[0,0,-1,1]  # 왼 오 위 아래
dy=[-1,1,0,0]
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))
print(bfs())

