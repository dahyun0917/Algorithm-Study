#BackJoon 15988 1,2,3 더하기 3
import sys

dp=[0,1,2,4]
for i in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    for j in range(len(dp),n+1):
        dp.append((dp[-3]+dp[-2]+dp[-1])%1000000009)
    print(dp[n])
