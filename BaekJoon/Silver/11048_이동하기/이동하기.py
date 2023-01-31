#BackJoon 11048 이동하기
import sys

N,M = map(int,sys.stdin.readline().split())
if N < 1 or M < 1 : dp=[[0 for _ in range(3)] for _ in range(3)]
else : dp=[[0 for _ in range(M)] for _ in range(N)]
graph=[]

for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))

dp[0][0]=graph[0][0]
for i in range(N):
    for j in range(M):
        if i-1 < 0 :
            dp[i][j]= graph[i][j]+dp[i][j-1]
        elif j-1 <0 :
            dp[i][j]= graph[i][j]+dp[i-1][j]
        else:
            dp[i][j]= graph[i][j]+max(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])

print(dp[N-1][M-1])
