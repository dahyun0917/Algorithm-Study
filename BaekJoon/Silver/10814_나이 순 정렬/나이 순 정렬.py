#BaekJoon 10814 나이 순 정렬
N=int(input())
nlist = [list(map(str,input().split())) for _ in range(N)]
nlist.sort(key= lambda x : int(x[0]))
for num , name in nlist:
    print(num,name)
