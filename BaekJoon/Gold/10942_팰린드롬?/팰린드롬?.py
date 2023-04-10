#BaekJoon 10942 팰린드롬?
import sys
input=sys.stdin.readline

def check(i,j):  # i번째에서 j까지 팰린드롬인지 확인
    while i<j:
        if nlist[i]==nlist[j]:
            i+=1
            j-=1
        else: return False
    return True

def che():
    for i in range(N,0,-1):  # 뒤에서부터 
        for j in range(i,N+1):
            if i==j : perin[i][j]=True  # 만약 i==j 즉, 한 개의 숫자만 본다면 True로
            elif i+1<N+1 and i+1<j-1 and nlist[i]==nlist[j]:  # 현재 i와 j의 값이 같고, i+1 ~ j-1 가 true라면 true임
                perin[i][j]=perin[i+1][j-1]
            else:                               # 아니라면 팰린드롬인지 전체 확인
                perin[i][j]=check(i,j)

N=int(input())    # N : 자연수 size
nlist=[0]+list(map(int,input().split()))  # nlist : 자연수
perin = [[False for _ in range(N+1)] for _ in range(N+1)]  # 팰린드롬 여부를 저장하는 배열
che()  # perin 초기화
M=int(input())
for _ in range(M):
    S,E = map(int,input().split())
    if perin[S][E] : print(1)
    else: print(0)

