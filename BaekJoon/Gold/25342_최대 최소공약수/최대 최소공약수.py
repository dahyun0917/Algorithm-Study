#BackJoon 25342 최대 최소공약수
import sys
from itertools import combinations
from math import lcm
from functools import reduce

for _ in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    if n%2!=0: print(lcm(n-2,n-1,n)) # 홀수일 시, [-2:] 가 정답
    else:
        result=0
        for c in list(combinations([n-3,n-2,n-1,n],3)):  # 짝수일 시 , [-3:] 중 세 개를 골라 max값을 찾으면 정답
            if result<reduce(lcm,c) : result=reduce(lcm,c)
        print(result)
