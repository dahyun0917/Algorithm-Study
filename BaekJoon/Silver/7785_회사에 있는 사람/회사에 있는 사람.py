#BackJoon 7785 회사에 있는 사람
import sys
n= int(sys.stdin.readline())
exist =set()

for _ in range(n):
    people=list(map(str,sys.stdin.readline().split()))
    if people[1] == 'enter': exist.add(people[0])
    elif people[1] == 'leave' : exist.remove(people[0])
exist=sorted(exist,reverse=True)
for e in exist:
    print(e)
    
