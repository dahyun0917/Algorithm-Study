#BaekJoon 1644 소수의 연속합
# 76640 KB / 2152 ms (Python 3)
# 162276 KB / 652 ms (pypy)
def era():   # 에라토스테네스의 체
    decimal_check[0],decimal_check[1]=False,False
    for i in range(2,N+1):
        if decimal_check[i] :
            decimal.append(i)
            j=2
            while j*i<=N:
                decimal_check[j*i]=False
                j+=1
N=int(input())  # 자연수
if N==1: print(0)
else:
    decimal_check=[True for _ in range(N+1)]  # 소수 확인 배열
    decimal=[]  # 소수 모아두기
    era()
    end=1
    sum=decimal[0]
    total=0
    for start in range(len(decimal)):   # 연속합 구하기 
        while end<len(decimal) and sum<N and start<=end:   # N보다 커질때까지 sum에 값 추가
            sum+=decimal[end]
            end+=1
        if sum==N : total+=1
        sum-=decimal[start]
    print(total)


