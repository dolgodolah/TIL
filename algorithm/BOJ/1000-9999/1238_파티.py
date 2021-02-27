# 첫번째 시도(정답 1224ms):모든 노드마다 X까지 가는데 걸리는 최소비용과 X에서 해당 노드로 가는 최소비용을 구한다.
# 즉 dijkstra를 N번 수행하게 된다.

# 두번째 시도(정답 196ms):하나의 단방향 그래프를 방향만 바꾸어 두 개의 그래프로 만들고
# X를 기준으로 두 그래프에 대해서 dijkstra를 한 번씩 수행한다.
# 그러면 각 노드들마다 X로 오는 최소비용과 X에서 각 노드들로 가는 최소비용이 구해지고
# 두 최소비용의 합 중 가장 큰 합이 X까지 가고 오는데 오래 걸리는 비용이다.

import sys
from heapq import heappop,heappush
input=sys.stdin.readline
N,M,X=map(int,input().split())

graph1=[[] for _ in range(N+1)]
graph2=[[] for _ in range(N+1)]
for _ in range(M):
    a,b,c=map(int,input().split())
    graph1[a].append((b,c))
    graph2[b].append((a,c))

def dijkstra(start,graph):
    queue=[]
    heappush(queue,(0,start))
    dist=[int(10e9)]*(N+1)
    dist[start]=0
    while queue:
        value,node=heappop(queue)
        if dist[node]<value:
            continue
        for i in graph[node]:
            if dist[i[0]]>dist[node]+i[1]:
                dist[i[0]]=dist[node]+i[1]
                heappush(queue,(dist[i[0]],i[0]))

    return dist

dist1=dijkstra(X,graph1)
dist2=dijkstra(X,graph2)
answer=0
for i in range(1,N+1):
    answer=max(answer,dist1[i]+dist2[i])
print(answer)



# 첫번째 시도(1224ms)
# graph=[[] for _ in range(N+1)]
# for _ in range(M):
#     a,b,c=map(int,input().split())
#     graph[a].append((b,c))

# def dijkstra(start,end):
#     queue=[]
#     heappush(queue,(0,start))
#     dist=[int(10e9)]*(N+1)
#     dist[start]=0
#     while queue:
#         value,node=heappop(queue)
#         if dist[node]<value:
#             continue
#         for i in graph[node]:
#             if dist[i[0]]>dist[node]+i[1]:
#                 dist[i[0]]=dist[node]+i[1]
#                 heappush(queue,(dist[i[0]],i[0]))

#     return dist[end]

# answer=0
# for i in range(1,N+1):
#     tmp=dijkstra(i,X)
#     tmp+=dijkstra(X,i)
#     answer=max(answer,tmp)
# print(answer)