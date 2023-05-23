#BaekJoon 2503 숫자 야구
import sys
input = sys.stdin.readline
nlist=[]
for _ in range(int(input())):
    nlist.append(list(map(int,input().split())))
count=0
for i in range(1,10):  # 첫번 째
    for j in range(1,10): # 두번 째
        if i==j : continue
        for k in range(1,10): # 세번 째
            result=True
            if i==k or j==k : continue
            for number,s,b in nlist:
                t1,t2,t3=str(number)
                i1,i2,i3=str(i),str(j),str(k)
                ts,tb=0,0
                if i1==t1 : ts+=1
                if i2==t2 : ts+=1
                if i3==t3 : ts+=1
                if i1==t2 or i1==t3 : tb+=1
                if i2==t1 or i2==t3 : tb+=1
                if i3==t1 or i3==t2 : tb+=1
                if ts!=s or tb!=b : result=False; break
            if result: count+=1
print(count)
                
