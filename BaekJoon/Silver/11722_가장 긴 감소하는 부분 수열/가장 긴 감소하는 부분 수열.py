#BackJoon 11722 가장 긴 감소하는 부분 수열
import sys
    
N=int(sys.stdin.readline())
matrix=[[0 for _ in range(N+1)] for _ in range(N+1)]
A=[-1]+list(map(int,sys.stdin.readline().split()))
dp=[1 for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(i+1,N+1):
        if A[i]>A[j]: dp[j]=max(dp[i]+1,dp[j])
print(max(dp))
