#BaekJoon 11720 숫자의 합
N=input()
nlist=input().strip()
sum=0
for i in range(len(nlist)):
    sum+=int(nlist[i])
print(sum)
