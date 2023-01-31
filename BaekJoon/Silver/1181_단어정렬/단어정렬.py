#BackJoon 1181 단어정렬
import sys
n=int(sys.stdin.readline())
length=[]
for i in range(n):
    text = sys.stdin.readline().strip()
    length.append([text,len(text)])
length=sorted(length,key=lambda x:(x[1],x[0]))

for i in range(n):
    if i!=0 and length[i][0]==length[i-1][0] : continue
    print(length[i][0])
