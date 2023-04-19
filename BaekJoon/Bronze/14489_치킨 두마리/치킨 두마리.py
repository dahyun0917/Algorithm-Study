#BaekJoon 14489 치킨 두마리
AB = list(map(int,input().split()))
C=int(input())
if sum(AB)==0 : print(0)
elif C==0 : print(sum(AB))
elif sum(AB)//C>=2: print(sum(AB)-C*2)
else: print(sum(AB))
