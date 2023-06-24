#BaekJoon 1920 수찾기
import sys
input = sys.stdin.readline
A=set()
N=int(input())
temp = list(map(int,input().split()))
for t in temp: A.add(t)
M = int(input())
Mlist=list(map(int,input().split()))
for m in Mlist: 
    if m in A: print(1)
    else: print(0)
