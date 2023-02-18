#BackJoon 2606 바이러스
import sys
sys.setrecursionlimit(10**9) # 재귀 깊이 늘려주기
def dfs(index):
    visited[index]=True
    for g in graph[index]:
        if visited[g] : continue
        else : 
            dfs(g)
    return 
    
def main():    
    global graph
    global visited
    computer_num=int(sys.stdin.readline())
    graph=[[] for _ in range(computer_num+1)]
    visited=[False for _ in range(computer_num+1)]
    for _ in range(int(sys.stdin.readline())):
        A,B = map(int,sys.stdin.readline().split())
        graph[A].append(B)
        graph[B].append(A)

    count=dfs(1)
    
    print(visited.count(True)-1)

main()
    
