#BaekJoon 10813 공 바꾸기
N,M=map(int,input().split())
bagu = [i for i in range(N+1)]
for _ in range(M):
    i,j = map(int,input().split())
    bagu[i],bagu[j]=bagu[j],bagu[i]
print(*bagu[1:])
