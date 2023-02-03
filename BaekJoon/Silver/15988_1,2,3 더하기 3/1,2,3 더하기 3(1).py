#BackJoon 15988 1,2,3 더하기 3
import sys

num=[]
n=int(sys.stdin.readline())

for _ in range(n):
    num.append(int(sys.stdin.readline()))

if max(num)<4 : dp=[0]*4
else : dp=[0]*(max(num)+1)

dp[0]=0
dp[1]=1
dp[2]=2
dp[3]=4

for i in range(4,max(num)+1):
    dp[i]=(dp[i-3]+dp[i-2]+dp[i-1])%1000000009

for i in num:
    print(dp[i])
