# 21년 5월 7일 두번째 풀이
from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people=deque(people)
    left=0
    right=len(people)-1
    while left<=right:
        if people[left]+people[right]<=limit:
            left+=1
        right-=1
        answer+=1
        
        
    return answer

# 21년 1월 24일 첫번째 풀이
# 문제 꼼꼼히 읽자!!!! 구명보트는 최대 2명밖에 못탄다..
# 해결 아이디어는 사람들을 몸무게 순으로 정렬을 하고
# 몸무게가 가장 작은 사람과 큰 사람을 태울거다.

# 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

# 위 제한사항으로 인해 가장 작은 사람이나 큰 사람 둘 중 한명은 무조건 보트를 탄다. (그러므로 while 한번 돌때마다 answer+1 해준다.)
# 주의할 점은 둘 중에 한명 태운다면 누구를 태울지이다.
# 조금만 생각해보면 쉽게 알 수 있다.
# solution([20,30,50,90],100)를 예로 들면 20,90 둘 중에 한명만 탈 수 있다.
# 20은 30이나 50과 보트를 탈 수 있는데 혼자 타버리면 손해다.(보트를 효율적으로 사용하지 못한다.)
# 즉 무거운사람이 먼저 타게끔 구현해주자.

def solution(people, limit):
    people.sort()
    answer=0
    left,right=0,len(people)-1 # 가장 가벼운 사람과 무거운 사람을 가르키는 변수이다.
    while left<right: 
        # 두 사람 모두 탈 수 없으면 무거운 사람만 태운다. (left+1을 하지 않는다.)
        if people[left]+people[right]<=limit: 
            left+=1
        right-=1
        answer+=1

    if left==right: #사람 한명이 남을 때가 있다. (아래 예제에 표시)
        answer+=1
    return answer

print(solution([40,40,40,40], 240))
print(solution([160, 150, 140, 60, 50, 40], 200))
print(solution([10,30,40,70,100], 110)) # 마지막에 사람 한명만 남는 경우
print(solution([20,30,50,90],100)) # 마지막에 사람 한명만 남는 경우