# 21년 5월 5일 두번째 풀이
def solution(record):
    answer = []
    logs = []
    dic = dict()
    for command in record:
        command = command.split()
        if command[0]=="Enter":
            logs.append((command[1],command[0])) #id, command종류
            if not command[1] in dic:
                dic[command[1]]=command[2]
            else:
                dic[command[1]]=command[2]
        elif command[0]=="Leave":
            logs.append((command[1],command[0]))
        else: # Change
            dic[command[1]]=command[2]


    for log in logs:
        if log[1]=="Enter":
            answer.append(str(dic[log[0]])+"님이 들어왔습니다.")
        else:
            answer.append(str(dic[log[0]]+"님이 나갔습니다."))
    return answer


# 21년 1월 28일 첫번째 풀이
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