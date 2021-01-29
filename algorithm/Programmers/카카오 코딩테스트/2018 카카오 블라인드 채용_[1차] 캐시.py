# 학교 운영체제 수업 때 들었던 LRU가 나오길래 띠용? 했다.
# LRU 내용을 상기시키려고 구글링했는데 가장 오랫동안 참조되지 않은 페이지를 교체하는 알고리즘이다.
# 캐시(queue) 안에 해당 city가 없으면 캐시 미스로 answer+=5를 해주고
# 가장 최근에 사용됐으므로 queue.append(city)를 해준다.
# 캐시(queue) 안에 해당 city가 있으면 캐시 히트로 answer+=1을 해주고
# LRU 알고리즘을 구현하기 위해서는 queue에서 해당 city를 꺼내 다시 append 해준다.
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    queue = deque()
    for city in cities:
        city=city.lower()
        if not city in queue: #cache miss
            answer+=5
            queue.append(city)
            if len(queue)>cacheSize:
                queue.popleft()
        else: #cache hit
            answer+=1
            queue.remove(city)
            queue.append(city)
    return answer

# print(solution(3,['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']))
print(solution(0,['Jeju', 'Pangyo', 'NewYork', 'newyork']))