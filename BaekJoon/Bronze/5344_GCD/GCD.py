#BackJoon 5344 GCD
import sys

def gcd(a,b):
    max=0
    if a<b:
        for i in range(1,(a//2)+1):
            if a%i==0 : 
                if max<i and b%i==0 : max=i
                if max<a//i and b%(a//i)==0 : max=a//i
    else:
        for i in range(1,(b//2)+1):
            if b%i==0 : 
                if max<i and a%i==0 : max=i
                if max<b//i and a%(b//i)==0 : max=b//i 
    return max
        
for _ in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split())
    print(gcd(a,b))
            
