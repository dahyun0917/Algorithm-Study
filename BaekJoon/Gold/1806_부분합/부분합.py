#BaekJoon 1806 부분합
N,S = map(int,input().split())
nlist=[0]+list(map(int,input().split())) # 인덱스 값으로 계산하기 때문에 조금 더 쉽게, 1~N까지 저장했어
total=nlist[1]  # 전체 값
j=2  # j : end
if total>=S: # 만약 첫번째 값이 바로 S넘으면 제일 최소인 1이기때문에 바로 반환
    print(1)
    exit()
else: length=N # 그게 아니면 최댓값이 N 길이기 때문에 초기화
for i in range(1,N+1):  # i : start   //start값 이동
    while total<S and j<=N: # total의 값이 S보다 커질때까지 계산
        total+=nlist[j]
        j+=1   # end 값 이동
    if i==1 and total<S and j>N: # 만약 첫번째부터 끝까지 전부 다 더했는데 total보다 작으면, 아예 가능성이 없기때문에 0출력 후, 종료
        print(0)
        exit()
    if total>=S: length=min(j-i,length) # total값이 S보다 크면 길이 최소값 구해주기
    total-=nlist[i] # nlist[start] 값 빼주기
print(length)
