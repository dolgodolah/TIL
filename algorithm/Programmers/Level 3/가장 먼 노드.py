# 기본 그래프 문제이다. bfs를 통해 모든 노드들을 탐색했고
# 노드들을 탐색할 때마다 딕셔너리를 통해 거리별로 카운팅을 했다.
# 딕셔너리 키들 중에 최댓값을 찾고 해당 키의 value를 반환한다.

from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(dic):
        queue=deque()
        queue.append((1,0))
        visited = [False]*(n+1)
        visited[1]=True
        while queue:
            node,cnt = queue.popleft()
            if cnt in dic:
                dic[cnt]+=1
            else:
                dic[cnt]=1
            for i in graph[node]:
                if visited[i]==False:
                    visited[i]=True
                    queue.append((i,cnt+1))
    dic=dict()
    bfs(dic)
    answer = dic[max(dic)]
    return answer
solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	)