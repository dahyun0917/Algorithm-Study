#BaekJoon 1005 ACM Craft
import sys
from collections import deque
input=sys.stdin.readline

def dijkstra(start):
    queue=deque()
    for i in range(len(start)):  
        queue.append(start[i])  # 시작 건물을 queue에 넣어준다
        distance[start[i]]=D[start[i]]  # 거리를 나타내는 배열 초기화 (시작건물을 짓는데 걸리는 시간으로 ! )
    while queue:
        node = queue.popleft()
        for g in graph[node]:
            if distance[g] < distance[node]+D[g]:  # 만약 해당 건물이 지어질 때, 전 건물의 건물 생성 시간이 큰 것을 저장해야 함
                distance[g]= distance[node]+D[g]
            parent[g]-=1  # 해당 건물의 부모를 줄여줌
            if parent[g]==0:  # 만약 부모가 0 즉, 시작 건물이 되었을 때,
                if g==W : return   # g가 최종 건설해야하는 건물이면, 바로 종료
                queue.append(g)  # queue에 g 추가
                

for _ in range(int(input())):
    N,K = map(int,input().split())  # N : 건물의 수, K : 순서 규칙 개수 
    D=[0]+list(map(int,input().split())) # D : 건설에 걸리는 시간
    graph=[[] for _ in range(N+1)]  # 모든 연결된 건물들 저장 그래프
    parent=[0 for i in range(N+1)]  # 부모 개수 저장 배열
    distance=[0 for _ in range(N+1)]  # 최단 거리 저장 
    started = []  # 부모 개수가 0인 건물들
    for _ in range(K):
        x,y = map(int,input().split())  #  x -> y : 건물 순서
        graph[x].append(y)   # weight 있는 graph임 즉, 순서가 있음
        parent[y]+=1  # y의 부모 개수 증가
    W = int(input())  # W : 건설해야할 최종 건물 
    for i in range(1,N+1):
        if parent[i]==0: started.append(i)  # 부모 개수가 0 인 건물들 저장
    dijkstra(started)  
    print(distance[W])
