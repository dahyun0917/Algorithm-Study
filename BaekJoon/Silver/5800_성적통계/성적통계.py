#BaekJoon 5800 성적통계
import sys
input = sys.stdin.readline
N=int(input())
for i in range(N):
    nlist = list(map(int,input().split()))
    nlist = sorted(nlist[1:],reverse=True)
    m = 0
    for j in range(1,len(nlist)) :
        m = max(m,nlist[j-1]-nlist[j])
    print("Class",i+1)
    # print("Max %d, Min %d, Largest gap %d" %(nlist[0],nlist[-1],m))
    print(f"Max {nlist[0]}, Min {nlist[-1]}, Largest gap {m}")
