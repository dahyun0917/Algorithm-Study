#BaekJoon 2018 수들의 합 5
N=int(input())
end=2
sum=1
result=0
for start in range(1,N+1):
    while  end<=N:
        if sum>=N: break
        sum+=end
        end+=1
    if sum==N: result+=1
    sum-=start
print(result)
