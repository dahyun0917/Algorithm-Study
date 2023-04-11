def solution(wallpaper):
    answer = []
    # print(wallpaper)
    start_j=1000000
    end_j=0
    start_i=1000000
    end_i=0
    # print(len(wallpaper))
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j]=='#':
                if start_i>=i : start_i=i
                if j<=start_j :
                    start_j=j
                if j>=end_j :
                    end_j=j+1
                if end_i<=i: 
                    end_i=i+1
    answer=[start_i,start_j,end_i,end_j]
    return answer
