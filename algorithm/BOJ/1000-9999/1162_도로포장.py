# 다익스트라를 활용해야하는 문제이다.
# N개의 노드에 대해서 M개의 간선이 주어질 때 1번노드에서 N번노드로 가는 최소비용은 다익스트라 기본이다.
# 문제는 최대 K번까지 간선의 비용을 0으로 할 수 있다는 점이다.

# 핵심 아이디어는 dist=[[int(10e9)*(K+1)] for _ in range(N+1)]이다.
# 노드 N개마다 최대 포장 횟수인 K만큼 dist를 만들어 주는 것이다.
# dist[N][0], dist[N][1], dist[N][2] ... dist[N][K] 의 의미는
# 1번노드에서 N번노드까지 가는데 도로포장을 0번 했을 때, 1번 했을 때, 2번 했을 때, ... K번 했을 때를 의미한다.

# 최종적으로는 dist[N]에서 최솟값이 정답이 된다.

import sys
from heapq import heappop,heappush
input=sys.stdin.readline
N,M,K=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

dist=[[int(10e9)]*(K+1) for _ in range(N+1)]
def dijkstra():
    queue=[]
    heappush(queue,(0,1,0)) #value,node,cnt(포장횟수)
    dist[1][0]=0
    while queue:
        value,node,cnt=heappop(queue)
        if dist[node][cnt]<value:continue
        for i in graph[node]:
            if cnt<K:
                if dist[i[0]][cnt+1]>value:
                    dist[i[0]][cnt+1]=value
                    heappush(queue,(dist[i[0]][cnt+1],i[0],cnt+1))
            if dist[i[0]][cnt]>value+i[1]:
                dist[i[0]][cnt]=value+i[1]
                heappush(queue,(dist[i[0]][cnt],i[0],cnt))
    return
dijkstra()
answer=int(10e9)
for i in range(K+1):
    answer=min(answer,dist[N][i])
print(answer)