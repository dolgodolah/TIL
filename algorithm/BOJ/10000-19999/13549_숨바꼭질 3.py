# 기존에 알고있었던 bfs알고리즘으로는 해결할 수 없었다.
# 0-1 bfs라는 새로운 개념을 알게되었다. 일반 bfs의 경우에는 간선의 가중치가 없는(동일한) 전제 조건이 필요하다.
# 하지만 이 문제의 경우 간선의 가중치가 0초와 1초가 있기 때문에 일반 bfs로 해결할 수 없다.
# 0-1 bfs는 가중치의 우선순위가 더 높은 간선을 큐의 맨 앞에 넣는 것이다.
# 즉, 0초가 걸리는 간선의 경우에는 queue.appendleft()를 통해 큐의 맨 앞에 추가하였다. (0초로 갈 수 있는 노드들부터 처리된다.)


from collections import deque

n,k=map(int,input().split())
visited=[int(10e9)]*100001
queue=deque()
queue.append((n,0))
visited[n]=0
while queue:
    x,sec=queue.popleft()
    if x-1>=0 and sec+1<visited[x-1]:
        visited[x-1]=sec+1
        queue.append((x-1,sec+1))
    if x+1<100001 and sec+1<visited[x+1]:
        visited[x+1]=sec+1
        queue.append((x+1,sec+1))
    if 2*x<100001 and sec<visited[2*x]:
        visited[2*x]=sec
        queue.appendleft((2*x,sec))

print(visited[k])