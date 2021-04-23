# 양방향으로 처리해주는 것만 유의하면 쉽게 풀 수 있다.

import sys
from collections import deque

input=sys.stdin.readline
n=int(input())
x,y=map(int,input().split())
m=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
answer=0
# print(graph)
def bfs():
    global answer
    queue=deque()
    queue.append((x,0))
    visited=[False]*(n+1)
    visited[x]=True
    while queue:
        node,cnt = queue.popleft()
        if node==y:
            answer=cnt
            return
        for i in graph[node]:
            if visited[i]==False:
                visited[i]=True
                queue.append((i,cnt+1))
    return

bfs()
if answer==0:
    print(-1)
else:
    print(answer)