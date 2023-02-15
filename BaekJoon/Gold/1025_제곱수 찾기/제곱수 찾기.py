#BackJoon 1025 제곱수 찾기
# 살짝 블로그 참고 (범위)
import sys
def bfss(x,y,n,m):
    text=str(table[x][y])
    if int(text)**0.5 == int(int(text)**0.5) : max=int(int(text)**0.5)
    else: max=-1
    while True:
        if 0<=x+n<N and 0<=y+m<M:
            text+=str(table[x+n][y+m])
            sqrt = float(text)**0.5
            if float(sqrt).is_integer() and max < sqrt : max=sqrt
            x+=n
            y+=m
        elif max==-1 : return max
        else: return int(max**2)


N,M = map(int,sys.stdin.readline().split())
table=[]
for _ in range(N):
    table.append(list(sys.stdin.readline().strip()))
if N==1 and M==1 and float(float(table[0][0])**0.5).is_integer() : max = table[0][0]
else: max=-1
for i in range(N):
    for j in range(M):
        for n in range(-N,N):
            for m in range(-M,M):
                if m==0 and n==0 : continue
                if 0<=i+n<N and 0<=j+m<M:
                    r = bfss(i,j,n,m)
                    if max<r : max=r
print(max)
