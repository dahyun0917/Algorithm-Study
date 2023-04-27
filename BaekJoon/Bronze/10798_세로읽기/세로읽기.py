#BaekJoon 10798 세로읽기
llist = [[] for _ in range(16)]
for _ in range(5):
    temp=list(map(str,input().strip()))
    for j in range(len(temp)):
        llist[j].append(temp[j])
for i in range(len(llist)):
    for j in range(len(llist[i])):
        print(llist[i][j],end='')
        
