import sys
from collections import deque
input = sys.stdin.readline
move_type = [-1,1,2]
n,k=map(int,input().split())
def solution(n):
    queue=deque()
    queue.append((n,0))
    visited = [False]*100001
    while queue:
        x,sec = queue.popleft()
        if x==k: #x의 위치가 k일 때 걸린 시간을 반환한다.
            return sec
        for dx in move_type:
            #각 위치를 최초방문할 때가 걸린 시간의 최솟값이기 때문에
            #방문처리를 수행함으로써 시간을 단축한다.
            if dx==2:
                if x*dx<=100000 and visited[x*dx]==False: 
                    nx = x*dx
                    queue.append((nx,sec+1))
                    visited[nx] = True
            else:
                if x+dx>=0 and x+dx<=100000 and visited[x+dx]==False:
                    nx=x+dx
                    queue.append((nx,sec+1))
                    visited[nx] = True
print(solution(n))
