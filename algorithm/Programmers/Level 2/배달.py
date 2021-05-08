from heapq import heappop,heappush

def dijkstra(start,end,N,graph):
    queue=[]
    heappush(queue,(0,start))
    dist=[int(10e9)]*(N+1)
    dist[start]=0
    while queue:
        value,node=heappop(queue)
        if dist[node]<value:continue
        for i in graph[node]:
            if dist[i[0]]>i[1]+value:
                dist[i[0]]=i[1]+value
                heappush(queue,(dist[i[0]],i[0]))

    return dist[end]

def solution(N, road, K):
    answer = 0
    graph=[[] for _ in range(N+1)]
    for i in road:
        graph[i[0]].append((i[1],i[2]))
        graph[i[1]].append((i[0],i[2]))

    for i in range(1,N+1):
        if dijkstra(1,i,N,graph)<=K:
            answer+=1

    return answer

# print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))
print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))