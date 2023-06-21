#BaekJoon 10988 팰린드롬인지 확인하기
n=input().strip()
start=0
end=len(n)-1
while start<end:
    if n[start]==n[end]: 
        start+=1
        end-=1
    else: 
        print(0)
        exit()
print(1)
