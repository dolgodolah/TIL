# 21년 5월 5일 두번째 풀이
from heapq import heappop, heappush
def check(scoville,K):
    for i in range(len(scoville)):
        if scoville[i]<K:
            return False
    return True

def solution(scoville, K):
    answer = 0
    queue=[]
    for value in scoville:
        heappush(queue,value)

    # 모든 음식의 스코빌 지수가 K이상이 아니고, 음식이 2개 이상일 때까지 계속 섞는다.
    while not check(queue,K) and len(queue)>1:
        v1=heappop(queue)
        v2=heappop(queue)*2
        heappush(queue,v1+v2)
        answer+=1 # 섞는 횟수 카운팅
    
    if check(queue,K):
        return answer
    else:
        return -1

print(solution([1, 2, 3, 9, 10, 12],7))


# 21년 1월 24일 첫번째 풀이
# scoville의 길이가 최대 1,000,000에다가 k가 최대 1,000,000,000이다.
# scoville를 매번 정렬하고 최소값을 꺼내면 시간초과가 예상된다.
# 힙구조를 이용하면 쉽게 구현할 수 있다.
# 다만 예외케이스를 잘 파악해야한다. (k=0이라서 음식을 섞지않아도 되는 경우)
# 나같은 경우는 scoville를 heappush하지않고 heappop으로 바로 이용해서 계속 오답이 떴다.

from heapq import heappop,heappush
def solution(scoville, K):
    answer = 0
    heap = [] # scoville를 힙정렬하기 위한 리스트
    for i in scoville:
        heappush(heap,i) # scoville를 힙구조로 정렬한다.

    # 음식을 섞기 전에 모든 음식의 스코빌 지수가 K이상이면 바로 0을 반환한다.
    for i in scoville:
        if not i>=K:
            break
    else:
        return 0

    # 음식을 더 이상 못섞을때까지(음식 하나 남을때까지) 반복한다.
    while len(heap)>1:
        a=heappop(heap)
        b=heappop(heap)
        heappush(heap,a+2*b)
        answer+=1

        for i in heap:
            if not i>=K:
                break
        else: # 모든 음식의 스코빌 지수가 K이상이면 answer을 반환한다.
            return answer

    return -1

print(solution([1,1,0],0))

