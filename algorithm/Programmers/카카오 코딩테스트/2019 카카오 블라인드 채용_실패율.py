#간단한 구현 문제이다. 실패율의 정의에 대해서만 잘 이해하고 풀면 된다.
#이 문제에서 실패율이란 '해당 스테이지에 정체된 사람/해당 스테이지를 도달한 사람(해당 스테이지에 정체된 사람+클리어 사람)'이다.

def solution(N, stages):
    answer = []
    fail = [] #각 스테이지별로 (스테이지번호,실패율)을 담는 리스트
    num=len(stages)
    for stage in range(1,N+1):
        if not num==0:
            a=stages.count(stage)#해당 stage를 클리어하지 못한 인원의 수
            fail.append((stage,a/num))#stage번호와 실패율을 담는다.
            num-=a #다음 stage의 실패율 계산을 위해 해당 stage를 클리어하지 못한 인원의 수는 제외해준다.
        else: #해당 stage에 도달한 사람이 없을 때(0으로 나누는 예외처리를 하기 위해)
            fail.append((stage,0))
    
    fail = sorted(fail,key=lambda x:(-x[1],x[0]))
    print(fail)
    for i in fail:
        answer.append(i[0])
    return answer

print(solution(5,[1,1,2]))