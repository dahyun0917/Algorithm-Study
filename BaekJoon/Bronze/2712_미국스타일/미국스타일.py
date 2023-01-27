#BackJoon 2712 미국스타일
import sys

n= int(sys.stdin.readline())

for _ in range(n):
    m = sys.stdin.readline().split()
    if m[1]=='kg' : print('{:.4f}'.format(round(float(m[0])*2.2046,4)),'lb')
    elif m[1]=='l' : print('{:.4f}'.format(round(float(m[0])*0.2642,4)),'g')
    elif m[1]=='lb' : print('{:.4f}'.format(round(float(m[0])*0.4536,4)),'kg') 
    elif m[1]=='g' : print('{:.4f}'.format(round(float(m[0])*3.7854,4)),'l')
