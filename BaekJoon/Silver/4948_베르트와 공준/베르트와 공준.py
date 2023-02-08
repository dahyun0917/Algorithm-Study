#BackJoon 4948 베르트와 공준
import sys
import math

def sieve_of_Eratosthenes(n):
    graph=[True for i in range(n+1)]
    for i in range(2, int(math.sqrt(n))+1):
        if graph[i]==True:
            j=2
            while i*j<=n:
                graph[i*j]=False
                j+=1
    return graph

list=[]    
while True:
    n = int(sys.stdin.readline())
    if n==0 : break
    list.append(n)

graph=sieve_of_Eratosthenes(max(list)*2)

for i in list:
    count=0
    for j in range(i+1,i*2+1):
        if graph[j] : count+=1
    print(count)
    
