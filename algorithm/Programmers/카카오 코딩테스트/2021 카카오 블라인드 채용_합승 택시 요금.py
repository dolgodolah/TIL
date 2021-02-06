# 다익스트라 알고리즘을 활용한 문제였다.
# 먼저 a,b를 택시 따로 타고 갔을 때의 가격을 구한다. dijkstra(출발지점,a도착지)+dijkstra(출발지점,b도착지)
# 그 후 노드를 하나씩 탐색하면서 해당 노드까지 같이 택시를 타고 그 이후는 따로 갔을 때의 비용을 구한다.
# dijkstra(출발지점,같이탈지점)+dijkstra(같이탈갈지점,a도착지)+dijkstra(같이탈지점,b도착지)그 비용이 최솟값이라면 갱신한다.

from heapq import heappop, heappush
graph = []
def dijkstra(start,end,n):
    dist = [int(10e9)]*(n+1)
    dist[start]=0
    queue = []
    heappush(queue,[0,start])
    while queue:
        value,node = heappop(queue)
        if dist[node]<value:continue #이 한줄이 효율성 테스트 통과를 시켰다.
        for i in graph[node]:
            if dist[i[0]]>dist[node]+i[1]:
                dist[i[0]]=dist[node]+i[1]
                heappush(queue,[dist[i[0]],i[0]])
    return dist[end]
def solution(n, s, a, b, fares):
    global graph
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        graph[fare[0]].append((fare[1],fare[2]))
        graph[fare[1]].append((fare[0],fare[2]))

    cost = dijkstra(s,a,n)+dijkstra(s,b,n)
    for i in range(1,n+1):
        if s!=i:
            cost = min(cost,dijkstra(s,i,n)+dijkstra(i,a,n)+dijkstra(i,b,n))
    
    return cost

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))