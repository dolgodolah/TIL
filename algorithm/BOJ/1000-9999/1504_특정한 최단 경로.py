# 다익스트라 알고리즘을 이용하여 풀 수 있다.
# 문제가 1에서 N까지 가는데 v1,v2를 꼭 들러야하고 그 때의 최소비용을 구하는 것인데
# 주의할 점은 1->v1->v2->N이 최소비용일 수 있고 1->v2->v1->N이 최소비용일 수 있다는 것이다.
# 둘다 구해서 더 작은 값을 정답으로 출력한다.

import sys
from heapq import heappop,heappush

N,E=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(E):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2=map(int,input().split())

def dijkstra(start,end):
    queue=[]
    distance=[int(10e9)]*(N+1)
    distance[start]=0
    heappush(queue,(0,start))
    while queue:
        value,node=heappop(queue)
        if distance[node]<value:
            continue
        for i in graph[node]:
            if distance[i[0]]>value+i[1]:
                distance[i[0]]=value+i[1]
                heappush(queue,(distance[i[0]],i[0]))
    return distance[end]

answer=min(dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,N),dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,N))
if answer>=int(10e9):
    print(-1)
else:
    print(answer)
