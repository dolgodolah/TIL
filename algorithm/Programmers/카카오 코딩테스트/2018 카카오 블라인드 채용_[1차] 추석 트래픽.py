# 혼자서 풀 때는 그렇게 안되는데 다른사람풀이보고 풀 때는 왜이리 쉬울까?
# 해결 아이디어 자체는 같은데 초단위를 처리하는 과정에 실수가 있었다.
# 시분초를 초단위로 바꿔주고 time_line의 시작과 끝마다 1초단위로 쪼개어
# 그 사이에 몇 개의 트래픽이 있는지 check해주면 된다.
def solution(lines):
    answer = 0
    time_line = []
    for line in lines:
        data = line.split()
        temp = data[1].split(":")
        end = int(temp[0])*3600 + int(temp[1])*60 + float(temp[2])
        start = end - float(data[2].replace('s','')) + 0.001
        time_line.append((round(start,3),round(end,3)))
    def check(time,time_line):
        result=0
        start = time
        end = start + 1
        for i in time_line:
            if i[1]>=start and i[0]<end:
                result+=1
        return result
    for i in time_line:
        answer=max(answer,check(i[0],time_line),check(i[1],time_line))
    return answer

print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
# print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
# print(solution([
# '2016-09-15 20:59:57.421 0.351s',
# '2016-09-15 20:59:58.233 1.181s',
# '2016-09-15 20:59:58.299 0.8s',
# '2016-09-15 20:59:58.688 1.041s',
# '2016-09-15 20:59:59.591 1.412s',
# '2016-09-15 21:00:00.464 1.466s',
# '2016-09-15 21:00:00.741 1.581s',
# '2016-09-15 21:00:00.748 2.31s',
# '2016-09-15 21:00:00.966 0.381s',
# '2016-09-15 21:00:02.066 2.62s'
# ]))