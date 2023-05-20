A,B=map(int,input().split())
C=int(input())
time = (A*60+B)+C
start=time//60
end=time%60
if end>=60 : start+=1; end%=60;
if start>=24: start%=24
print(start,end)
