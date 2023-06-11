#BaekJoon 1316 그룹단어체커
import sys
input = sys.stdin.readline
def check(word):
    use=set()
    last=word[0]
    use.add(last)
    for w in range(1,len(word)):
        if last==word[w]:continue
        if last!=word[w]: 
            if word[w] in use:  return False
            else: use.add(word[w]) 
        last=word[w]
    return True
result=0
for _ in range(int(input())):
    n = input().strip()
    if check(n) : result+=1
print(result)
    
