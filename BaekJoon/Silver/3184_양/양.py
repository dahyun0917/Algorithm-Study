#Baek Joon 3184 양
import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
def dfs(x,y):
    global wolf,sheep
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<R and 0<=ny<C and not visited[nx][ny] and field[nx][ny]!='#':
            visited[nx][ny]=True
            if field[nx][ny]=='v': wolf+=1
            elif field[nx][ny]=='o': sheep+=1
            dfs(nx,ny)
    return
    
dx = [1,-1,0,0]
dy = [0,0,1,-1]
R,C = map(int,input().split())
field = [list(map(str,input().strip())) for _ in range(R)]
visited=[[False for _ in range(C)] for _ in range(R)]
result=[0,0]
for i in range(R):
    for j in range(C):
        wolf,sheep=0,0
        if field[i][j]!='#' and not visited[i][j]:
            if field[i][j]=='v': wolf+=1
            elif field[i][j]=='o': sheep+=1
            visited[i][j]=True
            dfs(i,j)
        # print(i,j,": ",sheep,wolf)
        if wolf>=sheep: result[1]+=wolf
        else: result[0]+=sheep
print(*result)
