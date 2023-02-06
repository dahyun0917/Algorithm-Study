#BackJoon 1302 베스트셀러
import sys
input = sys.stdin.readline
dic = dict()

for _ in range(int(input())):
    text = input().strip()
    if text in dic : dic[text]+=1
    else : dic[text]=1

print(sorted(dic.items(),key=lambda item : (-item[1],item[0]))[0][0])
