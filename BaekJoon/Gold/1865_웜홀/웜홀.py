#BackJoon 1865 웜홀
import sys
input=sys.stdin.readline
INF=int(1e9)

def bf(start):
    dist[start]=0
    for i in range(N):
        for j in range(len(edges)):
            cur= edges[j][0]
            next_node=edges[j][1]
            cost=edges[j][2]
            if dist[cur]+cost <dist[next_node]:
                dist[next_node]=dist[cur]+cost
                if i==N-1 : return True  
    return False
       
for _ in range(int(input())):
    N,M,W = map(int,input().split())
    edges=[]
    dist=[INF]*(N+1)
    
    for i in range(M):
        S,E,T = map(int,input().split())
        for edge in edges:
            if edge[0]==S and edge[1]==E: 
                if edge[2]>T : edge[2]=T
            if edge[0]==E and edge[1]==S:
                if edge[2]>T : edge[2]=T
        else:
            edges.append([S,E,T])
            edges.append([E,S,T])
        
    for i in range(W):
        s,e,t = map(int,input().split())
        for edge in edges:
            if edge[0]==s and edge[1]==e:
                edge[2]-=t
        else: edges.append((s,e,-t))
    
    if bf(1): print("YES")
    else : print("NO")
    # for i in range(1,N+1):
    #     dist=[INF]*(N+1)
    #     bf(i)
    #     if min(dist)<0 : 
    #         print("YES")
    #         break
    # else:
    #     print("NO")
        
'''
코드 1
INF = 2000000000
모든 dist[v] = INF
dist[1] = 0
N-1번 반복:
  모든 v에 대해:
    모든 간선에 대해 최단거리 갱신
모든 v에 대해:
  모든 간선에 대해 최단거리 갱신
  갱신이 한 번이라도 일어났으면 true
'''     
