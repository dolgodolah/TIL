def solution(n):
    answer = 0
    for i in range(1,n+1): #i 시작 숫자
        s=0
        while s<n: #i부터 누적합이 n보다 작을때까지 반복하다가
            s+=i
            i+=1
        if s==n: #반복문이 끝났을 때 누적합이 n과 같으면 answer+1
            answer+=1
    return answer

print(solution(15))