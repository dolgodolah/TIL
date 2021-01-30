# 잔실수가 너무 많았던 문제이다.
# 주어진 조건에 맞추어 꼼꼼하게 구현하면 된다.

def solution(m, musicinfos):
    answer = ''
    # 조건이 일치하는 음악이 여러 개일 때 재생된 시간이 제일 긴 음악제목을 반환하기 위한 max_length
    max_length = 0 
    
    # 주어진 m을 #을 고려해서 리스트화 시킨다.
    list_m = []
    idx=0
    while idx<len(m):
        # 마지막 idx에서 idx+1을 하면 에러, 예외처리해주자.
        if idx<len(m)-1 and m[idx+1]=='#': 
            list_m.append(m[idx]+m[idx+1])
            idx+=1
        else:
            list_m.append(m[idx])
        idx+=1

    # 주어진 음악정보들에 대해서 분석해보자.
    for info in musicinfos:
        info = info.split(',')
        # 시작시간과 끝시간을 분단위로 바꿔주어 재생시간을 구한다.
        start = int(info[0][:2])*60+int(info[0][3:5])
        end = int(info[1][:2])*60+int(info[1][3:5])
        length = end-start # 재생시간
        
        # 해당 음악의 주어진 음을 재생시간에 맞춰 temp에 기록한다.
        # 예를 들어 'ABC#'을 7분동안 들었으면 'ABC#ABC#A'가 되도록 한다.
        idx = 0
        temp = ''
        while length>0:
            if idx<len(info[3])-1 and info[3][idx+1]=='#':
                temp+=info[3][idx]+info[3][idx+1]
                idx+=1
            else:
                temp+=info[3][idx]
            length-=1
            idx+=1
            if idx==len(info[3]):
                idx=0

        # temp에 기록된 음을 #을 고려해서 리스트화 시킨다.
        # 'ABC#ABC#A' -> ['A','B','C#','A','B','C#','A']
        ls = []
        idx = 0
        while idx<len(temp):
            if idx<len(temp)-1 and temp[idx+1]=='#':
                ls.append(temp[idx]+temp[idx+1])
                idx+=1
            else:
                ls.append(temp[idx])
            idx+=1
        
        # m이 ls안에 있는지 확인하고 그런 음악이 여러 개라면 재생시간이 가장 긴 음악을 정답으로 한다.
        # 재생시간도 같으면 먼저 입력된 음악을 정답으로 한다.
        for i in range(len(ls)):
            if list_m==ls[i:i+len(list_m)]:
                if end-start>max_length:
                    max_length=end-start
                    answer=info[2]

    if not answer:
        answer = "(None)"
    
    return answer


# print(solution('ABCDEFG',['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']	))
# print(solution('CC#BCC#BCC#BCC#B',['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']	))
print(solution('ABC',['13:00,13:05,HELLO,ABCDEF', '13:00,13:06,WORLD,ABCDEF']))
# print(solution('ABC',['23:13,23:14,HELLO,C#DEFGAB', '13:00,13:01,WORLD,ABCDEF']))

