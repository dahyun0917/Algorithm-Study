#BackJoon 10809 알파벳찾기
import sys
dic=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
text=list(map(str,sys.stdin.readline().strip()))

for i in range(len(dic)):
    if dic[i] in text : print(text.index(dic[i]),end=' ')
    else : print(-1,end=' ')
