#BackJoon 2822 점수계산
import sys

total=0
total_list=[]
list=[]

for _ in range(8):
    list.append(int(sys.stdin.readline()))

list_copy=list.copy()

for i in range(5):
    total+=max(list)
    total_list.append(list_copy.index(max(list))+1)
    list.remove(max(list))

total_list.sort()

print(total)
for i in range(len(total_list)):
    print(total_list[i],end=' ')
