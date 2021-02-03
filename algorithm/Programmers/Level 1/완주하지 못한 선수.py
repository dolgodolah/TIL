def solution(participant, completion):
    answer=''
    #참가자 명단 뽑아낸다.
    dic = dict()
    for name in participant:
        if name in dic:dic[name]+=1
        else:dic[name]=1

    #완주한 사람은 -1을 해준다.
    for name in completion:
        if name in dic:
            dic[name]-=1

    #완주못한 1명이 나오면 answer을 갱신하고 break
    for i in dic:
        if dic[i]==1:
            answer=i
            break
    
    return answer

solution(['mislav', 'stanko', 'mislav', 'ana'],['stanko', 'ana', 'mislav'])
