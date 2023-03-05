#BackJoon 2798 블랙잭
import sys
N,M = map(int,sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split()))
result=[]
for i in range(len(card)):
    for j in range(i+1,len(card)):
        for k in range(j+1,len(card)):
            total = card[i]+card[j]+card[k]
            if total==M: 
                print(M)
                exit()
            elif total<M:
                result.append(total)
print(sorted(result)[-1])
