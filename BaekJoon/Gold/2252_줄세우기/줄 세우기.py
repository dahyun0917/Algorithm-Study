#BackJoon 2252 줄 세우기
import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split()) # N : 학생 수 / M : 키 비교 횟수
graph=[[] for _ in range(N+1)]  # 연결된 그래프
indegree=[0 for _ in range(N+1)] # 진입노드 개수

for _ in range(M):
    A,B=map(int,input().split())
    graph[A].append(B)
    indegree[B]+=1

def topologycal_sort():
    queue=deque()
    
    for i in range(1,N+1): # 진입 노드 개수가 0개인 노드 찾아서 queue에 넣기
        if indegree[i]==0: 
            queue.append(i)
    
    while queue:
        q=queue.popleft()
        print(q)
        
        for g in graph[q]: # 해당 노드 q와 연결되어 있는 노드들
            indegree[g]-=1  # 연결되어 있는 노드의 진입 개수 하나 지우기
            if indegree[g]==0 : queue.append(g) # 만약 진입 개수가 0개 라면 queue에 추가
topologycal_sort()
