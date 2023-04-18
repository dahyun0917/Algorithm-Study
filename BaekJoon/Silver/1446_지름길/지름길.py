#BaekJoon 1446 지름길
import sys
N,D = map(int,sys.stdin.readline().split())
distance=[i for i in range(D+1)]
load = []
for _ in range(N):
    start,end,weight=map(int,sys.stdin.readline().split())
    if 0<=start<=D and 0<=end<=D: load.append((start,end,weight))
load.sort(key=lambda x:(x[0],x[1],x[2]))
for start,end,weight in load:
    if distance[end]>distance[start]+weight:
        distance[end]=distance[start]+weight
        for i in range(end+1,D+1):
            distance[i]=min(distance[i],distance[i-1]+1)
print(distance[D])
