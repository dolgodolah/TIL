# 첫번째 시도(시간초과) : dfs로 가능한 모든 경로를 탐색하여 그 중 원장선생님이 내게 될 최소의 돈을 구했다.
# 두번째 시도(340ms) : 이분탐색 + 그래프이론(bfs)

# 일단 이 문제를 해결하기 위해 그래프이론을 이용해야한다는 건 금방 생각할 수 있다.
# 하지만 그래프이론만으로는 시간초과를 해결할 수 없었다.
# 원장선생님이 내게 되는 최소의 돈(1이상 1,000,000이하)을 이분탐색해야한다.
# 해당 돈으로 그래프에서 1~목적지(N)까지 갈 수 있는지 없는지 bfs를 통해 판단한다.

# bfs로 탐색하기 위해서는 visited를 잘 활용해야하는데 이는 '백준 2206_벽부수고 이동하기'를 보면 좋다.
# condition에 따른 visited를 따로 처리해줘야한다. '백준 2206_벽부수고 이동하기'에서는 벽파괴여부,
# 이 문제에서는 공짜로 제공받는 케이블 수 K가 0보다 큰 지의 여부이다.
# 즉 visited=[[False]*(K+1) for _ in range(N+1)]로 초기화해야하고,
# visited[3][2]=True의 의미는 공짜로 제공받을 수 있는 케이블 수가 아직 2개 남았을 때 3번 컴퓨터의 방문을 했다는 뜻이다.



import sys
from collections import deque
input=sys.stdin.readline
N,P,K=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(P):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def bfs(limit):
    queue=deque()
    queue.append((1,K))
    visited=[[False]*(K+1) for _ in range(N+1)] # K의 condition에 따른 각 노드들의 방문 여부
    visited[1][K]=True # 공짜로 제공받을 수 있는 케이블이 K개일 때 1번 노드를 방문했다는 뜻
    while queue:
        node,cnt=queue.popleft()
        if node==N: # 목적지 N을 도착하면 해당 limit(원장선생님이 내야할 최소의 돈)으로 설치가 가능하다는 뜻이므로
            return True # True를 반환하여 원장선생님이 내야할 최소의 돈을 더 줄여본다.
        for i in graph[node]:
            if i[1]<=limit: # 원장선생님이 내야할 최소의 돈보다 작거나 같으면
                if visited[i[0]][cnt]==False: #cnt(K의 남은 횟수)를 줄이지 않고 방문여부를 판단한다.
                    visited[i[0]][cnt]=True
                    queue.append((i[0],cnt))
            else: # 원장선생님이 내야할 돈보다 크면 공짜로 제공받아야만 갈 수 있기 때문에
                if cnt>0 and visited[i[0]][cnt-1]==False: # 공짜 제공받을 수 있는 횟수가 0보다 큰지 확인하고 방문여부를 판단한다.
                    visited[i[0]][cnt-1]=True
                    queue.append((i[0],cnt-1))
    return False
left=0
right=1000001
answer=-1 #인터넷을 설치할 수 없을 때는 -1을 출력해야하므로 갱신되지 않았다면 -1을 그대로 출력할 수 있도록 -1로 초기화한다.
while left<=right:
    mid=(left+right)//2
    if bfs(mid):
        right=mid-1
        answer=mid
    else:
        left=mid+1
print(answer)