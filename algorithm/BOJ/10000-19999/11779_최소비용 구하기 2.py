# 다익스트라를 이용한 응용문제이다.
# 목적지까지의 최소비용은 기본 다익스트라로 구하면 되고, 목적지까지 가는데 지나가는 노드들을 구하는게 문제이다.
# visited=[0]*(n+1)을 만들어 해당 노드로 가기 위해서는 전에 어떤 노드를 갔는지 갱신하면 된다.
# 다익스트라 알고리즘을 이용하여 최소비용을 갱신할 때만 visited 값을 갱신하도록 했다.
# 예를 들어 3번노드에서 5번노드로 가는게 출발지점에서 5번지점으로 가는게 최소비용이라 할 때
# visited[5]=3으로 갱신한다. 즉 visited[5]=3이 의미하는 것은 5번 노드를 최소비용으로 갈 때 전 노드가 3번이라는 뜻이다.

# 출발지부터 목적지까지 경로를 담는 paht=[]를 만들어 목적지부터 넣고 목적지를 최소비용으로 갈 때 전 노드를 차례대로 추가한다.
# 즉, 정답을 출력할 때는 paht[::-1]을 출력해야한다.


import sys
from heapq import heappush,heappop
n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))


def dijkstra(start,end):
    global visited
    dist=[int(10e9)]*(n+1)
    dist[start]=0
    queue=[]
    heappush(queue,[0,start])
    while queue:
        value,node=heappop(queue)
        if dist[node]<value:continue
        for i in graph[node]:
            if dist[i[0]]>dist[node]+i[1]:
                dist[i[0]]=dist[node]+i[1]
                heappush(queue,[dist[i[0]],i[0]])
                visited[i[0]]=node
    # print(dist)
    # print(visited)
    return dist[end]
start,end=map(int,input().split())
visited=[0]*(n+1)
print(dijkstra(start,end))
path=[]

tmp=visited[end]
path.append(end)
while True:
    path.append(tmp)
    tmp=visited[tmp]
    if tmp==0:
        break
print(len(path))
print(*path[::-1])
    
