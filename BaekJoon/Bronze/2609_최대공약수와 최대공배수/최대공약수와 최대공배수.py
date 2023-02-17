#BackJoon 2609 최대공약수와 최대공배수
import sys
def gcd(x,y):
    while y!=0:
        x,y=y,x%y
    return x

A,B = map(int,sys.stdin.readline().split())
print(gcd(A,B))
print(A*B//(gcd(A,B)))
