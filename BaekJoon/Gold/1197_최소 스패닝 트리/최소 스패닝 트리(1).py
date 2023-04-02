#BaekJoon 1197 최소 스패닝 트리
# 54108 KB / 648 ms
import sys
from queue import PriorityQueue
input = sys.stdin.readline


def root(i):   # root노드 찾기
    while i!= ids[i]: i = ids[i]
    return i
def connected(a,b):  # 두 노드가 연결되어 있는지 확인
    return root(a)==root(b)
def union(a,b):   # 두 노드 연결 , 이때 최적화를 시키기 위해 size를 사용(size가 더 작은 노드를 큰 노드 밑에 삽입)
    a,b = root(a),root(b)
    if size[a]<=size[b]:
        ids[a]=ids[b]
        size[b]+=size[a]
    else:
        ids[b]=ids[a]
        size[a]+=size[b]
        
V,E = map(int,input().split())
ids=[i for i in range(V+1)]
size=[1 for _ in range(V+1)]
pq = PriorityQueue()  
graph_use=[]   # 연결된 노드의 개수를 알기 위한 배열 (정수로 수정해도 될듯 !)
weight_sum =0   # 최값 스패닝 트리의 값

for _ in range(E):
    A,B,C = map(int,input().split())
    pq.put((C,A,B))   # 가중치가 가장 작은 노드부터 계산하기 위해 pq에 C를 가장 앞에 넣는다.
while not pq.empty() and len(graph_use)<=V-1:
    c,a,b=pq.get()
    if not connected(a,b):
         union(a,b)
         weight_sum+=c
         graph_use.append((a,b))
         
print(weight_sum)
