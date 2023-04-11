def solution(book_time):
    room_list=[]
    book_time.sort(key= lambda x:x[0])
    print(book_time)
    for time in book_time:
        c1 , m1 = time[0].split(':') # 시작 시간
        start_time= int(c1)*60+int(m1)  # 분으로 변경
        c2 , m2 = time[1].split(':') # 종료 시간
        end_time = int(c2)*60+int(m2)  # 분으로 변경
        print("시간 : ",c1,m1,start_time,c2,m2,end_time)
        for i in range(len(room_list)):
            # print(room_list , start_time)
            if room_list[i]<=start_time : 
                room_list[i]=end_time+10
                # print("다음",i)
                # print((end_time+10)//60 , end_time%60)
                break
        else: 
            room_list.append(end_time+10)
            # print("추가")
            # print((end_time+10)//60 , end_time%60)
            
        
    # print(room_list)
    return len(room_list)
