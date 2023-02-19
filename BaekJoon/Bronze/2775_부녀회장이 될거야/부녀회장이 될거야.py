#BackJoon 2775 부녀회장이 될거야
import sys
for i in range(int(sys.stdin.readline())):
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    table=[[k for k in range(n+1)] for _ in range(k+1)]
    for j in range(1,k+1):
        for o in range(1,n+1):
            table[j][o]=sum(table[j-1][:o+1])
    print(table[k][n])
