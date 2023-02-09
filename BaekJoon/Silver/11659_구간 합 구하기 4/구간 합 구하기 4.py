#BackJoon 11659 구간 합 구하기 4
import sys
N,M=map(int,sys.stdin.readline().split())

nlist=list(map(int,sys.stdin.readline().split()))
for i in range(1,N):  # 누적 합을 저줌
    nlist[i]+=nlist[i-1]
for i in range(M):
    a,b=map(int,sys.stdin.readline().split())  # 인덱스 값을 구분하기 위해 계산할 때 -1을 추가로 더 해줌
    if a-2<0 : print(nlist[b-1])  
    else : print(nlist[b-1]-nlist[a-2])
    
