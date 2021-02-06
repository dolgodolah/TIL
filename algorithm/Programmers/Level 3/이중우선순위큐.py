# 파이썬의 heapq 라이브러리를 사용하여 쉽게 풀이하였다.
# minheqp만 구현되기때문에 최댓값을 제거할 때는 remove(max(queue))를 사용했다.
from heapq import heappop, heappush
def solution(operations):
    answer = []
    queue = []
    for operation in operations:
        ls = operation.split(" ")
        if ls[0]=='I':
            num = int(ls[1])
            heappush(queue,num)
        elif ls[0]=='D' and ls[1]=='-1':
            if queue:
                heappop(queue)
        elif ls[0]=='D' and ls[1]=='1':
            if queue:
                queue.remove(max(queue))
    if queue:
        answer = [max(queue),min(queue)]
    else:
        answer = [0,0]

     

    return answer

# print(solution(["I 7","I 5","I -5","D -1"]))
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))