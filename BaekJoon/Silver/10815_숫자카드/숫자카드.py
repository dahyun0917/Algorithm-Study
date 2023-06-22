#BaekJoon 10815 숫자카드
N=int(input())
slist = set(map(int,input().split()))
M = int(input())
for m in list(map(int,input().split())):
    if m in slist: print("1",end=' ')
    else: print("0",end=' ')
