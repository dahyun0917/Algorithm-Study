#BackJoon 16953 A->B
import sys
sys.setrecursionlimit(10**9) # 재귀 깊이 늘려주기
def dfs(a,b,count):
    if a>=b: return a, count
    temp_a1 , t_c1 = dfs(a*2,b,count+1)
    temp_a2 , t_c2 = dfs(int(str(a)+'1'),b,count+1)
    if temp_a1 == b and temp_a2 ==b:
        if t_c1<t_c2 : return temp_a1,t_c1
        else : return temp_a2, t_c2
    elif temp_a1 == b : return temp_a1, t_c1
    elif temp_a2 == b : return temp_a2, t_c2
    else : return 0,0
def main():
    A,B = map(int,sys.stdin.readline().split())
    result_a, result_count = dfs(A,B,1)
    if result_a == B : print(result_count)
    else : print(-1)

main()
