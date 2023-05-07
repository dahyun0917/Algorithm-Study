#BaekJoon 6236 용돈관리
# 블로그 참고 - min, max 범위 틀림
import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000000)
def check(k):
    get = 1
    have = k
    for i in range(N):
        if have<money[i]:
            get+=1
            have=k
            if get>M: return False
        have-=money[i]
    return True
        
def find(a,b):
    global result
    if a>b : return
    mid = (a+b)//2
    if check(mid) and mid>=max(money): 
        result=mid
        find(a,mid-1)
    else: find(mid+1,b)
        
        
N,M = map(int,input().split())
money = [int(input()) for _ in range(N)]
result=100000000
find(min(money),sum(money))
print(result)
'''
5 1
1
3
5
7
9
=> 25

5 4
100
100
100
100
100
=> 200

5 5
1
1
1
1
100
=> 100

2 2
500
501
=> 501
'''
