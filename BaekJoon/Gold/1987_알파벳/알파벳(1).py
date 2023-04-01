#BaekJoon 1987 알파벳
import sys

def bfs():
    global result
    # visited=[[False for _ in range(C)] for _ in range(R)]
    # visited[0][0]=True
    queue=set([(0,0,board[0][0])])  # 세로, 가로, 방문한 알파벳의 집합, count , 방문여부
    while queue:
        x,y,alpha=queue.pop()
        visited_index=False  # 더 이상 갈 수 있는지 여부
        # visited_temp=[]+visited  # 세미 방문 여부 
        # visited_temp=copy.deepcopy(visited)  # 세미 방문 여부
        for i in range(4):  # 상하좌우 봄
            nx,ny=x+directionX[i],y+directionY[i]  # 다음 이동할 좌표  ( nx : 세로 , ny : 가로)
            if 0<=nx<R and 0<=ny<C and not board[nx][ny] in alpha:
                # visited_temp[nx][ny]=True
                visited_index=True
                queue.add((nx,ny,alpha+board[nx][ny]))
        if not visited_index and result<len(alpha): result=len(alpha)

directionX=[0,0,-1,1]  # 상하좌우
directionY=[-1,1,0,0]
R,C = map(int,sys.stdin.readline().split())  # R : 세로 , C : 가로
board=[]   # 보드
result=1 # 결과값
result_temp=[]
visited=[[False for _ in range(C)] for _ in range(R)]
for i in range(R):
    board.append(list(map(str,sys.stdin.readline().strip())))
bfs()
print(result)
