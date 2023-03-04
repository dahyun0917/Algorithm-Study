#BackJoon 2231 분해합
import sys
N=int(sys.stdin.readline())
M=N//2
while M<N:
    total=M
    for t in str(total):
        total+=int(t)
    if total==N : 
        print(M)
        break
    M+=1
else: print(0)
