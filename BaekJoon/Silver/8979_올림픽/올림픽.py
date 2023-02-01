#BackJoon 8785 올림픽
import sys

N,K = map(int,sys.stdin.readline().split())
rank = []
for _ in range(N):
    rank.append(list(map(int,sys.stdin.readline().split())))

rank=sorted(rank,key=lambda x: (-x[1],-x[2],-x[3]))
index=0
for i in range(N):
    if rank[i][0]==K : index=i

for i in range(N):
    if rank[index][1:]==rank[i][1:] and index>i: 
        index=i
        break
print(index+1)
