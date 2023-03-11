#BackJoon 1246 온라인 판매
import sys
input=sys.stdin.readline
customer_list=[]
N,M = map(int,input().split())
for _ in range(M):
    customer_list.append(int(input()))
customer_list.sort(reverse=True)
max_money=0
pay=0
for i in range(M):
    if i+1>N: break
    if max_money<((i+1)*customer_list[i]) : 
        max_money=(i+1)*customer_list[i]
        pay=customer_list[i]
print(pay,max_money)

