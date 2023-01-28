#BackJoon 2822 점수계산
import sys

total=0
total_list=[]
list=[]

for _ in range(8):
    list.append(int(sys.stdin.readline()))

list_copy=list.copy()
list_copy.sort(reverse=True)

for i in range(5):
    total+=list_copy[i]
    total_list.append(list.index(list_copy[i])+1)

total_list.sort()

print(total)
for i in range(5):
    print(total_list[i],end=' ')
