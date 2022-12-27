#BackJoon 3303 킹, 퀸, 룩, 비숍, 나이트, 폰

dong = list(map(int,input().split()))
chess = [1,1,2,2,2,8]


for i in range(0,6):
    if i==5 : print(chess[i]-dong[i])
    else: print(chess[i]-dong[i] , end=' ')
