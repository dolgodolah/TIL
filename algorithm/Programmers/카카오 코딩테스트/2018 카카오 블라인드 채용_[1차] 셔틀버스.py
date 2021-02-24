# timetable에서 주어진 시간들을 분단위로 바꾸어 (인덱스 번호+1)와 함께 queue에 저장한다.
# ["08:00", "08:01"] -> [(480,1),(481,2)]

# 콘의 도착시간(answer)을 0(00:00)에서부터 탐색하여
# 주어진 셔틀 운행 횟수(n), 셔틀 운행 간격(t), 한 셔틀에 탈 수 있는 최대 크루 수(m) 조건에 맞게
# 사무실에 도착할 수 있는지 확인한다.(도착할 수 없을 때 까지)

from collections import deque
def solution(n, t, m, timetable):
    answer = 0
    queue = []
    for i in range(len(timetable)):
        hour,minute=timetable[i].split(":")
        value=int(hour)*60+int(minute) #timetable에 있는 시간들을 분단위로 바꿔 value값으로 치환한다.
        queue.append((value,i+1)) #idx값과 함께 queue에 저장한다.
    
    while True:
        values=queue.copy()
        values.append((answer,0)) #콘의 도착시간과 인덱스 값을 추가한다.
        values=deque(sorted(values,key=lambda x:x[0])) #도착시간만 기준으로 하여 오름차순 정렬한다.
        # print(values)
        now=540 #첫 셔틀버스의 도착시간은 09:00이고 이를 value로 치환하면 540이다.
        check=False
        for _ in range(n): # 셔틀 운행 횟수만큼 반복한다.
            for _ in range(m): # 한 셔틀버스마다 m명을 태울 수 있다.
                if values[0][0]<=now: # 가장 앞 줄에 서있는 사람의 value가 현재 시간 값보다 작거나 같으면 탈 수 있다.
                    value,idx=values.popleft() 
                    if idx==0: # 해당 사람이 콘이라면
                        check=True # check를 True로 바꾸준다.
                        break
            if check==True: #check가 True라면 콘이 해당 도착시간에 사무실을 도착할 수 있다는 것이다.
                answer+=1 #도착시간을 1분씩 늘려보자.
                break
            now+=t # 해당 셔틀 버스에서 m명을 모두 태웠으면 셔틀 운행 간격만큼 더해줘 now를 다음 셔틀 도착시간으로 바꿔준다.
        
        if check==False: # 셔틀 운행 횟수만큼 모두 탐색했는데 콘이 셔틀버스를 타지못했다면 check는 False일 것이다.
            break # while문을 종료한다.
    answer-=1 # 해당 시간에서 셔틀 버스를 타지못했으므로 answer-=1
    

    # 구해진 answer을 출력 형식에 맞게 바꿔준다.
    hour=str(answer//60)
    minute=str(answer%60)
    if len(hour)==1:
        hour='0'+hour
    if len(minute)==1:
        minute='0'+minute
    answer=hour+':'+minute

    return answer


# print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"]))
# print(solution(2,10,2,['09:10', '09:09', '08:00']))
print(solution(1,1,5,['00:01', '00:01', '00:01', '00:01', '00:01']))