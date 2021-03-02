# 트리의 지름 구하는 공식 -> 임의의 한 점에서 가장 먼 노드를 구하고 그 노드에서 가장 먼 노드를 구한다.

from collections import deque
n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def bfs(x):
    queue=deque()
    queue.append((x,0))
    visited=[False]*(n+1)
    visited[x]=True
    result=[x,0]
    while queue:
        node,value=queue.popleft()
        if result[1]<value:
            result=[node,value]
        for i in graph[node]:
            if visited[i[0]]==False:
                visited[i[0]]=True
                queue.append((i[0],value+i[1]))
    return result
print(bfs(bfs(1)[0])[1])