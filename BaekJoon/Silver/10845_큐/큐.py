#BackJoon 10845 큐
import sys

n=int(sys.stdin.readline())
queue=[]

for _ in range(n):
    text=sys.stdin.readline()
    if "push" in text:
        push = text.split()
        queue.append(push[1])
    elif "pop" in text:
        if len(queue)==0: print("-1") 
        else: print(queue.pop(0))
    elif "size" in text: print(len(queue))
    elif "empty" in text:
        if len(queue)==0: print("1")
        else: print("0")
    elif "front" in text:
        if len(queue)==0: print("-1")
        else: print(queue[0])
    elif "back" in text:
        if len(queue)==0: print("-1")
        else: print(queue[-1])
