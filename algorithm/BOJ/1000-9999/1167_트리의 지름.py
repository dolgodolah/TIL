# 첫번째 시도(시간초과) : 모든 노드마다 bfs(혹은 dfs)를 수행해 가장 긴 거리를 출력한다.
# 두번째 시도(정답) : 임의의 노드에서 bfs(혹은 dfs)를 수행해 가장 긴 거리를 반환하는 노드를 구하여, 해당 노드에서의 가장 긴 거리를 출력한다. (트리의 지름 공식이라고 한다.)

# 임의의 노드와 해당 임의의 노드에서 가장 긴 거리를 반환하는 노드는 트리 지름의 일부이다.
# 그러므로 임의의 노드에서 가장 긴거리를 반환하는 노드에서 가장 긴거리를 반환하는 노드까지의 거리가 트리의 지름이다.

from collections import deque

V=int(input())
graph=[[] for _ in range(V+1)]
for _ in range(V):
    info=list(map(int,input().split()))
    for i in range(1,len(info)-2,2):
        graph[info[0]].append((info[i],info[i+1]))

def bfs(x):
    result=0
    max_dist=0
    queue=deque()
    queue.append((x,0))
    visited=[False]*(V+1)
    visited[x]=True
    while queue:
        node,dist=queue.popleft()
        if max_dist<dist:
            max_dist=dist
            result=node
        for i in graph[node]:
            if visited[i[0]]==False:
                visited[i[0]]=True
                queue.append((i[0],dist+i[1]))
    return result,max_dist

result=bfs(1)
answer=bfs(result[0])
print(answer[1])


# def dfs(x,visited,dist):
#     global max_dist
#     global result
#     visited[x]=True
#     if max_dist<dist:
#         max_dist=dist
#         result=x
#     for i in graph[x]:
#         if visited[i[0]]==False:
#             dfs(i[0],visited,dist+i[1])
#             visited[i[0]]=False

# max_dist=0
# result=0
# visited=[False]*(V+1)
# dfs(1,visited,0)
# visited=[False]*(V+1)
# dfs(result,visited,0)
# print(max_dist)