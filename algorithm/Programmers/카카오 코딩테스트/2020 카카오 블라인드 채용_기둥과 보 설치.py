# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

# 위 조건을 항상 생각하면서 구현해주면 된다.
# 처음에는 n크기만큼 board 2차원 리스트를 생성해 build_frame에서 주어진 좌표값마다 처리를 해주었다.
# 설치 단계는 순조로웠으나 삭제 단계에서는 위 조건 만족여부를 판별하기 위해서는 
# 삭제 연산이 들어올 때마다 n*n을 매번 탐색해줘야한다는걸 알았다.(시간초과 예상)
# 일단 위 조건 만족여부를 판별해주는 check 함수를 만들었고
# n*n board를 탐색하는 것이 아니라 build_frame에서 주어진 좌표값들을 그대로 answer에 추가해
# answer의 길이만큼만 탐색해주도록 했다.

# 위 조건에서 설명된 말들을 조건식으로 표현하는 것이 중요하다.
# "기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다."를 조건식으로 그대로 써보면
# if y==0 or [x,y,1] in answer or [x-1,y,1] in answer or [x,y-1,0] in answer 이다.
# 위 if 조건문 중 하나라도 맞으면 해당 (answer에 담긴)build_frame에 대해서는 조건을 만족한다는 것이다.
# 여기서 return True를 했었는데 이럴 경우에는 다른 build_frame에 대해서는 조건 만족여부를 확인할 수 없다.
# 그래서  if y!=0 and not [x,y,1] in answer and not [x-1,y,1] in answer and not [x,y-1,0] in answer로 바꿔주고
# 위 if 조건문을 다 만족한다면 return False, 모든 (answer에 담긴)build_frame이 무사히 조건문을 통과하면 return True을 한다.


def solution(n, build_frame):
    answer = []
    def check(answer):
        for x,y,a in answer:
            if a==0: #기둥
                if y!=0 and not [x,y-1,0] in answer and not [x-1,y,1] in answer and not [x,y,1] in answer:
                    return False
            elif a==1: #보
                if not [x,y-1,0] in answer and not [x+1,y-1,0] in answer and (not [x-1,y,1] in answer or not [x+1,y,1] in answer):
                    return False
        return True

    for x,y,a,b in build_frame:
        if b==1: #설치
            answer.append([x,y,a])
            if check(answer)==False:
                answer.remove([x,y,a])
        elif b==0: #삭제
            answer.remove([x,y,a])
            if check(answer)==False:
                answer.append([x,y,a])
        # print(answer)        
    answer.sort()
    return answer

print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]	))