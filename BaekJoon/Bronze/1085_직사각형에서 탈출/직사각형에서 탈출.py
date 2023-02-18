#BackJoon 1085 직사각형에서 탈출
import sys
x,y,w,h = map(int,sys.stdin.readline().split())
print(min(abs(w-x),abs(h-y),abs(x-0),abs(y-0)))
