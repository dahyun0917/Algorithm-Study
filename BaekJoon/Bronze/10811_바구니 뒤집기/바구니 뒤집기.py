#BaekJoon 10811 바구니 뒤집기
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
ba = [i for i in range(N+1)]
for i in range(M):
    i,j = map(int,input().split())
    ba[i:j+1]=reversed(ba[i:j+1])
    
print(*ba[1:])
