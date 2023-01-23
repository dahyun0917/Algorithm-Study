#BackJoon 1363 1로 만들기
#2는 1, 10은 3, 572은 10, 40은 5, 642은 10
import sys
n = int(sys.stdin.readline())
if n<4 : dp=[0]*10
else: dp=[0]* (n+1)

dp[1]=0
dp[2]=1
dp[3]=1

for i in range(4,n+1):
    if i%2==0 and i%3==0:
        dp[i]= min(dp[i-1]+1,dp[i//2]+1,dp[i//3]+1)
    elif i%2==0 :
        dp[i]= min(dp[i-1]+1,dp[i//2]+1)
    elif i%3==0:
        dp[i]= min(dp[i-1]+1,dp[i//3]+1)
    else:
        dp[i]=dp[i-1]+1
print(dp[n])



