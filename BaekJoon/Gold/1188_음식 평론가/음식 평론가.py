#BackJoon 1188 음식 평론가
#블로그 참고
import sys
import math
N,M = map(int,sys.stdin.readline().split())

if N>=M and N%M==0 : print(0)
else : print(M-math.gcd(N,M))

# 3차 코드
# if N%M==0 and N>=M: print(0)
# elif N<M and M%N==0 : print(N*((M//N)-1))
# else : print(M-1)

# 2차 코드
# if N>=M : 
#     if N%M==0 : print(0) # 6 / 2
#     else : print(M-1) # 8 / 5
# else:
#     if M%N==0 : print(N*((M//N)-1))  # 2 / 6
#     else : print(M-1)   # 3 / 4
    
    # if M%N==0 : print((M//gcd)+(N//gcd))
    # elif (N/M)<1 : print(N)
    # else : print(m+n)
    


# 1차 코드
# if M<N :
#     if N%M==0 : print(0)
#     else : print(math.ceil(M/N))
# elif M/N>0 : print(math.ceil(1+M/N))
