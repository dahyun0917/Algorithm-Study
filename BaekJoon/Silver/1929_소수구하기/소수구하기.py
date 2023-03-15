#BackJoon 1929 소수구하기
import sys
def era():
    sosu=[True for i in range(1000001)]
    sosu[0]=False
    sosu[1]=False
    for i in range(2,1000001):
        if sosu[i] :
            j=2
            while j*i < 1000001:
                sosu[i*j]=False
                j+=1
    return sosu
decimal=era()
M,N=map(int,sys.stdin.readline().split())
for i in range(M,N+1):
    if decimal[i] : print(i)
