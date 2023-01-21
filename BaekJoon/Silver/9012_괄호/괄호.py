#BackJoon 9012 괄호
import sys

n= int(sys.stdin.readline())
vps_in = []

for _ in range(n):
    vps = sys.stdin.readline()
    vps_in.clear()
    for i in range(len(vps)):
        if(vps[i] == '('):
            vps_in.append('(')
        elif(vps[i] == ')'):
            if(len(vps_in)==0):
                # print('NO')
                vps_in.append("NO")
                break
            vps_in.pop()
    if(len(vps_in)==0):
        print("YES")
    else: print("NO")
