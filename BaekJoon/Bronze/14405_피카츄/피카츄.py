#BaekJoon 14405 피카츄
pikachu = ['pi','ka','chu']
nlist = input()
result=''
for i in range(len(nlist)):
    result+=nlist[i]
    if result in pikachu: result=''
    # if len(result)>3 : print("NO"); exit()
if result!='' : print("NO")
else: print("YES")
