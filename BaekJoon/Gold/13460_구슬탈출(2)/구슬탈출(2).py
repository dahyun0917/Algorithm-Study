#BaekJoon 13460 구슬탈출(2)
import sys
from collections import deque
def move(x,y,dx,dy):  # 움직일 수 있을만큼 움직이기
    count=0
    while 0<=x+dx<N  and 0<=y+dy<M:
        if board[x+dx][y+dy]=='O':  # 만약 구멍으로 빠지면 return
            return x+dx,y+dy,count+1
        elif board[x+dx][y+dy]!='#':  # 장애물이 없을 시 이동
            x+=dx; y+=dy
            count+=1
        else: break # 장애물이 있을 시 멈춤
    return x,y,count
def bfs():
    queue=deque()
    queue.append((Rx,Ry,Bx,By,0))
    visited=[[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visited[Rx][Ry][Bx][By]=True
    while queue:
        rX,rY,bX,bY,depth = queue.popleft()
        if depth==10 : return -1  # 10번 이상 움직였으면 -1 리턴
        for i in range(4):
            rx,ry,cnt_r = move(rX,rY,dx[i],dy[i])
            bx,by,cnt_b = move(bX,bY,dx[i],dy[i])
            if board[bx][by]=='O': continue  # 파란공이 0에 들어갔을 때, 바로 continue (해당 경우는 더 이상 보지 않겠다)
            if board[rx][ry]=='O': return depth+1  # 빨간공은 0 들어갔을 때, return
            if rx==bx and ry==by :  # 똑같은 위치일 경우
                if cnt_r > cnt_b :   # 만약 빨간공이 더 멀리서 왔으면
                    rx-=dx[i];ry-=dy[i]
                elif cnt_r < cnt_b :   # 만약 파란공이 더 멀리서 왔으면
                    bx-=dx[i];by-=dy[i]
            if not visited[rx][ry][bx][by]:  # 해당 위치를 방문하지 않았을 시, 방문처리하고 queue에 추가
                visited[rx][ry][bx][by]=True
                queue.append((rx,ry,bx,by,depth+1))
    return -1   # 더 이상 갈 곳이 없으므로 -1 리턴

        
N,M = map(int,sys.stdin.readline().split())
board = []
Rx,Ry = 0,0
Bx,By = 0,0
dx=[0,0,-1,1]  # 좌 우 상 하
dy=[-1,1,0,0]
for i in range(N):
    board.append(list(map(str,sys.stdin.readline().strip())))
    for j in range(M):
        if board[i][j]=='R': Rx = i; Ry = j
        if board[i][j]=='B': Bx = i; By=j
print(bfs())
            
