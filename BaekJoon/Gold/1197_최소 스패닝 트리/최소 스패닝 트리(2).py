#BaekJoon 1197 최소 스패닝 트리
# 시간초과 남 ㅠㅠ
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))
def dfs(start):
    global count
    visited[start]=True
    for end in graph[start]:
        if not visited[end] and (start,end) in g_set:
            count+=g_set[(start,end)]
            dfs(end)        
    
V,E = map(int,input().split())
graph=[[] for _ in range(V+1)]
g_set={}
visited=[]
for _ in range(E):
    A,B,C = map(int,input().split())
    if (A,B) in g_set : 
        g_set[(A,B)]=min(g_set[(A,B)],C)
    else: 
        g_set[(A,B)]=C
        graph[A].append(B)
        graph[B].append(A)

result=2147483648
for i in range(1,V+1):
    count=0
    visited.clear()
    visited=[False for _ in range(V+1)]
    dfs(i)
    if count!=0 : result=min(result,count)
if result!=2147483648: print(result)
else: print(0)
