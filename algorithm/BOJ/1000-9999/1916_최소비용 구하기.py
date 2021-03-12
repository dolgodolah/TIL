#다익스트라 알고리즘
#단반향그래프라는 점만 주의하자

import sys
from heapq import heappop, heappush
input=sys.stdin.readline
n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start,end):
    queue=[]
    heappush(queue,(0,start))
    dist=[int(10e9)]*(n+1)
    dist[start]=0
    while queue:
        value,node=heappop(queue)
        if dist[node]<value:continue
        for i in graph[node]:
            if dist[i[0]]>dist[node]+i[1]:
                dist[i[0]]=dist[node]+i[1]
                heappush(queue,(dist[i[0]],i[0]))
    
    return dist[end]
start,end=map(int,input().split())
print(dijkstra(start,end))