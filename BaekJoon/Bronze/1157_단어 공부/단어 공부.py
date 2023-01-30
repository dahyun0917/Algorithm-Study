#BackJoon 1157 단어 공부
import sys
text=list(map(str,sys.stdin.readline().strip()))
dic=dict()
for t in text:
    up=t.upper()
    if up in dic:
        dic[up]=dic[up]+1
    else:
        dic[up]=1

max=0
temp=True
for key in dic.keys():
    if max<dic[key]:
        max=dic[key]
        alp=key
        temp=True
    elif max==dic[key]: temp=False
if temp:print(alp)
else: print("?")
        
    
