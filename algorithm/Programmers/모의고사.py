#1번 수포자, 2번 수포자, 3번 수포자의 답 패턴을 이용하는 문제이다.
#처음 풀이할때는 시험이 최대 10,000문제라는 점을 활용해서 미리 [1,2,3,4,5]*2000을 선언해줬다.
#공간복잡도가 올라가는 대신 속도가 빠르다.
#두번째 풀이는 패턴을 통해 나머지값을 인덱스로 이용하는것이다.

#최대 범위만큼 미리 선언
def solution(answers):
    one=[1,2,3,4,5]*2000
    two=[2,1,2,3,2,4,2,5]*1250
    three=[3,3,1,1,2,2,4,4,5,5]*1000
    scores=[0,0,0]
    answer = []
    for i in range(len(answers)):
        if one[i]==answers[i]:
            scores[0]+=1
        if two[i]==answers[i]:
            scores[1]+=1
        if three[i]==answers[i]:
            scores[2]+=1
    max_score = max(scores)
    for i in range(3):
        if scores[i]==max_score:
            answer.append(i+1)
    return answer

#나머지값을 인덱스로 이용
def solution(answers):
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    scores=[0,0,0]
    answer = []
    for i in range(len(answers)):
        if answers[i]==one[i%len(one)]:
            scores[0]+=1
        if answers[i]==two[i%len(two)]:
            scores[1]+=1
        if answers[i]==three[i%len(three)]:
            scores[2]+=1
    max_score = max(scores)
    for i in range(3):
        if scores[i]==max_score:
            answer.append(i+1)
    return answer
print(solution([1,3,2,4,2]))
