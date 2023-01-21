#BackJoon 10828 스택
import sys 
n=int(sys.stdin.readline())
stack=[]

for _ in range(n):
    text = sys.stdin.readline()
    if("push" in text):
        stack.append(text.split()[1])
    elif("pop" in text):
        if len(stack)==0:
            print("-1")
        else:
            print(stack.pop())
    elif("size" in text):
        print(len(stack))
    elif("empty" in text):
        if len(stack)==0:
            print("1")
        else:
            print("0")
    elif("top" in text):
        if len(stack)==0:
            print("-1")
        else:
            print(stack[-1]) 
    
