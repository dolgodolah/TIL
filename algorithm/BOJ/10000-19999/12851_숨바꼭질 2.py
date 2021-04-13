# 첫번째 시도 (틀렸습니다) : 수빈이의 처음 위치인 visited[n]을 0으로 초기화하지 않았다.
# 두번째 시도 (220ms) : bfs로 동생의 위치 k를 몇 번 방문하는지 구한다. x에서 이동을 한 nx는 최초방문이거나 이동횟수가 같을 때만 이동가능하다.

from collections import deque
n,k=map(int,input().split())
visited=[int(10e9)]*100001
visited[n]=0
answer=0
def bfs(n,k):
    global answer
    queue=deque()
    queue.append((n,0))
    while queue:
        x,cnt=queue.popleft()
        if x==k:
            answer+=1
        for nx in [x+1,x-1,x*2]:
            if nx<100001 and nx>=0 and nx<100001:
                if visited[nx]>=cnt+1:
                    visited[nx]=cnt+1
                    queue.append((nx,cnt+1))
bfs(n,k)
print(visited[k])
print(answer)

