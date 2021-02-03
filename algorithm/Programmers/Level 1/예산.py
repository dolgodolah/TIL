def solution(d, budget):
    answer = 0
    d = sorted(d)
    temp = 0
    for i in d:
        temp+=i
        answer+=1
        if temp>budget:
            answer-=1
            break
    return answer

print(solution([2,2,3,3],10))