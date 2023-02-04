#BackJoon 11656 접미사 배열
import sys
S = sys.stdin.readline().strip()
text=[]
for i in range(len(S)):
    text.append(S[i:])
text.sort()
for t in text:
    print(t)
