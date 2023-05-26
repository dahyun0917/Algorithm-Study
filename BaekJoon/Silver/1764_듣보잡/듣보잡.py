#BaekJoon 1764 듣보잡
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
nlist=set()
result=[]
for _ in range(N):
    nlist.add(input().strip())
for _ in range(M):
    m = input().strip()
    if m in nlist : result.append(m)
print(len(result))
for r in sorted(result):
    print(r)
