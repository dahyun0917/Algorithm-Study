#BaekJoon 17087 숨바꼭질6
import sys
def gcd(x,y):
    while y!=0:
        x,y=y,x%y
    return x
N,S = map(int,sys.stdin.readline().split())
A_list = list(map(int,sys.stdin.readline().split()))
result=0
for i in range(len(A_list)) :
    if i>=1:  result=gcd(result,abs(A_list[i]-S))
    else : result=abs(A_list[i]-S)
print(result)
    
