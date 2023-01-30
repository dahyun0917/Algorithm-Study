#BackJoon 11047 동전0

import sys

N,K=map(int,sys.stdin.readline().split())
k_list=[]
count=0

for _ in range(N):
    k_list.append(int(sys.stdin.readline()))

for i in reversed(k_list):
    count += K//i
    K= K%i
    
print(count)
