# 1을 시작으로 bfs를 수행하면 각 노드들마다 부모를 알 수 있다.

import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

root=[1]*(n+1)

def bfs():
    queue=deque()
    queue.append(1)
    visited=[False]*(n+1)
    visited[1]=True
    while queue:
        node=queue.popleft()
        for i in graph[node]:
            if visited[i]==False:
                visited[i]=True
                queue.append(i)
                root[i]=node

bfs()
for i in range(2,n+1):
    print(root[i])