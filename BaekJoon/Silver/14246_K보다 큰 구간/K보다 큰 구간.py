#BackJoon 14246 K보다 큰 구간
import sys

n=int(sys.stdin.readline())
nlist=list(map(int,sys.stdin.readline().split()))
k=int(sys.stdin.readline())

count=0
sum=0
end=0

for start in range(n):
    while sum<=k and end<n : # sum이 k보다 작고 end가 n보다 작을 때
        sum+=nlist[end]  # nlist[end]까지를 sum에 더한다
        end+=1
    if sum>k : count+=(n-end+1) # 만약 sum이 k보다 크다면 end ~ n 까지 인덱스 값을 count에 더해준다
    sum-=nlist[start] # 다음 start값부터 확인해야하므로 현재 nlist[start]값을 sum에서 빼준다
        
print(count)
