#BackJoon 9613 GCD 합
import sys
from math import gcd

# def gcd(a,b):   # 직접 gcd 구하기
#     max=0
#     if a<b:
#         for i in range(1,(a//2)+1):
#             if a%i==0 : 
#                 if max<i and b%i==0 : max=i
#                 if max<a//i and b%(a//i)==0 : max=a//i
#     else:
#         for i in range(1,(b//2)+1):
#             if b%i==0 : 
#                 if max<i and b%i==0 : max=i
#                 if max<b//i and a%(b//i)==0 : max=b//i 
#     return max
        
tlist=[]
for _ in range(int(sys.stdin.readline())):
    tlist.clear()
    tlist = list(map(int,sys.stdin.readline().split())) # tlist에 t 입력받기
    total_gcd=0  # gcd 합 저장할 변수
    for i in range(1,len(tlist)):   # 이중배열 돌며 모든 쌍의 gcd 구하기
        for j in range(i+1,len(tlist)):
            total_gcd+=gcd(tlist[i],tlist[j])
   
    print(total_gcd)
