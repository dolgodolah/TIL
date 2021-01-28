#userId에 대한 정보를 딕셔너리에 저장해 닉네임이 바뀌면 해당 id의를 찾아 닉네임을 바꿔주도록 한다.
#record가 들어오면 Enter,Leave,Change에 대한 정보와 userId의 정보만 따서 log에 담는다.
#change의 경우 dic[userId]의 값을 해당 닉네임으로 바꾸는 처리를 해준다.
#record에 대한 처리가 다 끝났으면 log의 값들을 result에 담는다.

def solution(record):
    log = []
    user = dict()
    answer = []
    for i in record:
        i=i.split()
        if i[0]=='Enter':
            if not i[1] in user:
                user[i[1]]=i[2] 
            else:
                user[i[1]]=i[2]
            log.append([i[0],i[1]])
        elif i[0]=='Leave':
            log.append([i[0],i[1]])
        elif i[0]=='Change':
            user[i[1]]=i[2]

    for i in log:
        if i[0]=='Enter':
            answer.append(f"{user[i[1]]}님이 들어왔습니다.")
        elif i[0]=='Leave':
            answer.append(f"{user[i[1]]}님이 나갔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))