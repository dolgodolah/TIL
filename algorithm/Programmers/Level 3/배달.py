from heapq import heappop,heappush

def dijkstra(start,n,graph):
    dist = [int(10e9)]*(n+1)
    dist[start]=0
    queue = []
    heappush(queue,[0,start])
    while queue:
        value,node = heappop(queue)
        if dist[node]<value:continue
        for i in graph[node]:
            if dist[i[0]]>dist[node]+i[1]:
                dist[i[0]]=dist[node]+i[1]
                heappush(queue,[dist[i[0]],i[0]])
    return dist

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    for i in road:
        graph[i[0]].append((i[1],i[2]))
        graph[i[1]].append((i[0],i[2]))
    # print(graph)
    dist = dijkstra(1,N,graph)
    for i in range(1,len(dist)):
        if dist[i]<=K:
            answer+=1

    return answer

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))



