#BackJoon 2961 도영이가 만든 맛있는 음식
# 블로그 참조 - 조합사용하는 것 인식 
import sys
from itertools import combinations

Total=[] # 조합을 사용할 배열  :  인덱스를 대상으로 조합 구할 예정
SList=[] # 입력받은 신맛 재료
BList=[] # 입력받은 쓴맛 재료

result=1000000000

for i in range(int(sys.stdin.readline())):
    S,B=(map(int,sys.stdin.readline().split()))
    SList.append(S)
    BList.append(B)
    Total.append(i)
    result=min(result,abs(S-B))  # 입력받은 S와 B의 차이로 result에 최소값 저장

for i in range(2,len(Total)+1):  # 2 ~ 입력받은 값
    total=list(combinations(Total,i))  # i개의 모든 조합 리스트로 반환
    # 조합으로 구한 인덱스를 기준으로 SList와 BList에 접근하여 최솟값 저장
    for j in total:  
        s=1 # 신 맛
        b=0 # 쓴 맛
        for k in j:
            s*=SList[k]
            b+=BList[k]
        result=min(result,abs(s-b))


print(result)
