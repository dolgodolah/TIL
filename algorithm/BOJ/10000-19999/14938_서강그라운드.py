# 다익스트라

from heapq import heappop,heappush
import sys
input=sys.stdin.readline
n,m,r=map(int,input().split())
items=list(map(int,input().split()))
graph=[[] for _ in range(n+1)]
for _ in range(r):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    queue=[]
    heappush(queue,(0,start))
    dist=[int(10e9)]*(n+1)
    dist[start]=0
    while queue:
        value,node=heappop(queue)
        if dist[node]<value:
            continue
        for i in graph[node]:
            if dist[i[0]]>value+i[1]:
                dist[i[0]]=value+i[1]
                heappush(queue,(dist[i[0]],i[0]))
    return dist

def get_item(dist):
    result=0
    for i in range(1,n+1):
        if dist[i]<=m:
            result+=items[i-1]
    return result
answer=0
for i in range(1,n+1):
    answer=max(answer,get_item(dijkstra(i)))
print(answer)