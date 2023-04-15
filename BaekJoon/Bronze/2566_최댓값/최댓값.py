#BaekJoonn 2566 최댓값
import sys
nlist=[]
max_num=0
max_i,max_j=0,0
for i in range(9):
    nlist.append(list(map(int,sys.stdin.readline().split())))
    for j in range(9):
        if nlist[i][j]>max_num:
            max_num=nlist[i][j]
            max_i=i;max_j=j
print(max_num)
print(max_i+1,max_j+1)
