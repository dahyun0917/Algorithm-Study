#BackJoon 3052 나머지
import sys
s = []
for i in range(10):
    n=int(sys.stdin.readline())
    if (n%42) in s : continue
    s.append(n%42)
print(len(s))
