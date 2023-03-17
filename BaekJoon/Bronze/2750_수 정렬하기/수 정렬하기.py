#BaekJoon 2750 수 정렬하기
import sys
N=int(sys.stdin.readline())
for n in sorted([int(input()) for i in range(N)]):
    print(n)
