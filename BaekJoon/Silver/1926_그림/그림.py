# #BackJoon 1926 그림
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m : return 0
    
    if graph[x][y]==1:
        graph[x][y]=0
        count=1
        count+=dfs(x-1,y)
        count+=dfs(x+1,y)
        count+=dfs(x,y-1)
        count+=dfs(x,y+1)
        return count
    return 0
    
n,m=map(int,sys.stdin.readline().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

result=0
max=0
for i in range(n):
    for j in range(m):
        count = dfs(i,j)
        if count>0: 
            result+=1
            if max<count: max=count
print(result)
print(max)
