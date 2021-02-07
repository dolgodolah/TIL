# 해결 기본 아이디어는 가장 큰 수를 줄여나가는 것이다.
# 처음에는 max(works)를 통해서 가장 큰 값을 찾고 해당 인덱스를 찾은 후 그 인덱스에 있는 값을 -1 해줬다.
# 이 풀이는 효율성 테스트를 통과하지 못했다.
# 그 다음 바로 생각해낸 풀이가 heapq를 이용한 풀이이다.
# heapq를 응용해 max heap을 구현하였다.
from heapq import heappop, heappush
def solution(n, works):
    answer = 0
    queue = []
    for work in works:
        heappush(queue,(-work,work))
    for _ in range(n):
        tmp = heappop(queue)
        if tmp==(0,0):
            heappush(queue,(tmp[0],tmp[1]))
            break
        heappush(queue,(tmp[0]+1,tmp[1]-1))
    for i in queue:
        answer+=i[1]**2
    return answer

print(solution(4,[4,3,3]))
print(solution(1,[2,1,2]))
print(solution(3,[1,1]))