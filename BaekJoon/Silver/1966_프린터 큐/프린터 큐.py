#BackJoon 1966 프린터 큐
import sys
from queue import Queue
input=sys.stdin.readline
for _ in range(int(input())):
    count=1
    Q = Queue() 
    N,M = map(int,input().split())  # N : 문서의 개수 , M : 궁금한 문서의 위치(인덱스)
    nlist = list(map(int,input().split()))
    for i in range(len(nlist)):
        Q.put((nlist[i],i))  # Q에 하나씩 추가 (중요도 , 위치)
    while Q.qsize() :
        q=Q.get()
        if q[0]<max(nlist): Q.put((q[0],q[1]))  # nlist의 가장 큰 값보다 중요도가 작으면 Q 맨 뒤에 다시 추가
        elif q[1]==M :  # 위치가 같다면 프린트 후 종료
            print(count)
            break
        else : # count 증가 , nlist에서 삭제해주기
            count+=1 
            nlist.remove(q[0])
    
