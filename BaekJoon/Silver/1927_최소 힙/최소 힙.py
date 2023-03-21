#BaekJoon 1927 최소 힙
import sys
import heapq
queue=[]
for i in range(int(sys.stdin.readline())):
    x=int(sys.stdin.readline())
    if x!=0: heapq.heappush(queue,x)
    elif x==0 and len(queue)==0: print(0)
    else : print(heapq.heappop(queue))
