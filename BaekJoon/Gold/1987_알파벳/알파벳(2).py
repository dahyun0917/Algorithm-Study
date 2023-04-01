#BaekJoon 1987 알파벳
# 276596 KB / 7428 ms
# pypy로 돌림
import sys
sys.setrecursionlimit(int(1e5))

def dfs(x,y,alpha,visited):
    global result
    visited_index=False
    for i in range(4):
        nx,ny=x+directionX[i],y+directionY[i]  # 다음 이동할 좌표  ( nx : 세로 , ny : 가로)
        if 0<=nx<R and 0<=ny<C and not board[nx][ny] in alpha:
            alpha.add(board[nx][ny])
            dfs(nx,ny,alpha,visited)
            alpha.discard(board[nx][ny])
    if not visited_index : result=max(result,len(alpha))
            

directionX=[0,0,-1,1]  # 상하좌우
directionY=[-1,1,0,0]
R,C = map(int,sys.stdin.readline().split())  # R : 세로 , C : 가로
board=[]   # 보드
result=1 # 결과값
visited=[[False for _ in range(C)] for _ in range(R)]
for i in range(R):
    board.append(list(map(str,sys.stdin.readline().strip())))
dfs(0,0,set([board[0][0]]),visited)
print(result)

