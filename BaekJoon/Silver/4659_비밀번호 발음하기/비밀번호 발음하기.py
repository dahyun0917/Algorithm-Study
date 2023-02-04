#BackJoon 4659 비밀번호 발음하기
import sys

vowel=['a','e','i','o','u']

while True:
    text=sys.stdin.readline().strip()
    if text=='end': break
    v=0
    c=0
    Perfect=False
    for i in range(len(text)):
        if text[i] in vowel : 
            v+=1
            c=0
            Perfect=True
        else :
            c+=1
            v=0
        if v>2 or c>2 or (text[i]!='e' and text[i]!='o' and (i!=len(text)-1 and text[i]==text[i+1])):
            Perfect=False
            break
    if Perfect==False : print(f'<{text}> is not acceptable.')
    else : print(f'<{text}> is acceptable.')
        
    
