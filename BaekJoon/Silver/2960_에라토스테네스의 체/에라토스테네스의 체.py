#BackJoon 2960 에라토스테네스의 체
import sys
def decimal(N,K):
    de_list = [True for _ in range(N+1)] 
    de_list[0]=False
    de_list[1]=False
    count=0
    for i in range(2,N+1):
        if de_list[i] :
            j=1
            while j*i<=N:
                if de_list[j*i]==False: 
                    j+=1
                    continue
                de_list[j*i]=False
                count+=1
                if count==K : print(j*i)
                j+=1
            
        
N,K=map(int,sys.stdin.readline().split())
decimal(N,K)
