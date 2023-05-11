#BaekJoon 12026 BOJ 거리
N=int(input())
nlist=list(map(str,input().strip()))
dp=[10000000000000 for _ in range(N)]
dp[0]=0
for i in range(1,N):
    for j in range(i):
        if (nlist[i]=='B'and nlist[j]=='J') or (nlist[i]=='O' and nlist[j]=='B') or (nlist[i]=='J' and nlist[j]=='O'):
            dp[i]=min(dp[i],dp[j]+pow((i-j),2))
if dp[N-1]>=10000000000000: print(-1)
else: print(dp[N-1])
