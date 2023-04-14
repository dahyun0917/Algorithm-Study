alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # 알파벳 순서
def solution(s, skip, index):
    answer=[]
    for i in s:
        start=alpha.index(i)
        count=0
        while True:
            if start>=25: start=0 # z
            else: start+=1
            
            if not alpha[start] in skip: count+=1
            if count==index:
                answer.append(alpha[start])
                break
          
    # print(''.join(answer))         
    return ''.join(answer)
