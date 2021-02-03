# 체육복을 잃어버린 학생들을 탐색하여 해당 학생의 앞뒷번호가 여벌체육복을 가지고 있는지 확인한다.
# 여벌체육복을 확인할 때는 앞번호부터 확인한다.(오름차순의 경우)
# 예를들어 1~5번 학생들의 체육복 상황이 [2, 0, 2, 0, 1]라고 하자.
# 2번째 학생이 체육복이 없기때문에 앞뒷번호가 여벌체육복을 가지고 있는지 확인해야하는데
# 뒷번호부터 할 경우 4번째 학생이 빌릴 체육복이 없어져 최댓값이 되지못한다.

# 이대로만 구현해서 냈더니 3개가 실패뜬다. 문제를 다시 읽어보니
# 여별체육복을 가져온 학생들 중에 도난을 당한 학생도 있다고 한다.(2벌 가져왔는데 1벌 도난당함)
# 이 학생에 대해서는 예외처리를 해줘야한다. 
# 예외케이스 n=2, lost=[1], reserve=[1], 첫번째학생이 도난을 당했지만 여별이 있으므로 최댓값은 2이다.

def solution(n, lost, reserve):
    answer = n-len(lost) #전체학생수에서 체육복을 도난당한 학생수를 빼준다.

    #도난당했지만 여벌이 있는 학생에 대한 예외처리(위에서 도난당한 학생수를 빼버렸으므로)
    temp = []
    for i in lost: #도난 당한 학생 중에
        if i in reserve: #여벌 가져왔던 학생들은
            temp.append(i) #temp에 추가해주고
            answer+=1 #여벌이 있기때문에 answer은 +1해준다.
    
    for i in temp:#temp에 있던 학생들에 대한 처리를 해준다.
        lost.remove(i)
        reserve.remove(i)

    for i in lost: #도난 당한 i번째 학생의
        if i-1 in reserve: #앞번호가 여벌이 있다면
            reserve.remove(i-1)
            answer+=1
        elif i+1 in reserve: #뒷번호가 여벌이 있다면
            reserve.remove(i+1)
            answer+=1
    return answer

print(solution(2,[1], [1]))
