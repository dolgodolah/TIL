# 출발지점에서 도착지점까지 가는 모든 경로를 탐색해야된다고 생각해서 바로 백트래킹(dfs)를 생각했다.
# 테스트케이스 반절 이상이 시간초과가 발생했다.
# 풀이를 보니 bfs로도 접근이 가능했다. bfs는 방문처리를 통해 방문했던 지점은 다시 못가지만
# 해당 지점까지의 cost를 저장해서 더 작은 cost가 들어올때는 다시 방문할 수 있게 해주고 갱신해줌으로써 완전탐색이 가능했다.
# 주의할 점은 (0,0)에서 출발할 때 오른쪽으로 출발하는 경우와 아래로 출발하는 경우 두가지가 있으므로 2번 탐색해줘야한다.

# (0,0)에서 두 방향으로 탐색을 어떻게 하느냐에 따라서 반례가 생길 수 있다. (하지만 테스트 케이스는 모두 통과한다..)
# bfs(0,0,0,0) #x,y,direction,cost
# bfs(0,0,1,0)
# 이렇게 두 방향을 각각 탐색하는 방법이 있고,

# bfs():
#   ...
#   queue.append((0,0,0,0))
#   queue.append((0,0,1,0))
# 이렇게 두 방향을 동시에 탐색하는 방법이 있다.

# 전자의 경우가 반례없이 모두 통과하는 가장 좋은 방법이고
# 후자는 반례가 있지만 테스트 케이스는 모두 통과하는 경우이다.
from collections import deque
move = [(-1,0,0),(1,0,0),(0,-1,1),(0,1,1)]

def solution(board):
    answer = 0
    def bfs(x,y,direction,cost):
        n = len(board)
        queue = deque()
        queue.append((x,y,direction,cost))
        visited = [[0]*n for _ in range(n)]
        visited[0][0]=1
        while queue:
            x,y,direction,cost = queue.popleft()
            for i in range(4):
                nx=x+move[i][0]
                ny=y+move[i][1]
                d=move[i][2]
                if 0<=nx<n and 0<=ny<n and board[nx][ny]==0:
                    if d==direction:
                        if visited[nx][ny]==0 or cost+100<=visited[nx][ny]:
                            visited[nx][ny]=cost+100
                            queue.append((nx,ny,direction,cost+100))
                    else:
                        if visited[nx][ny]==0 or cost+600<=visited[nx][ny]:
                            visited[nx][ny]=cost+600
                            queue.append((nx,ny,(direction+1)%2,cost+600))
        # for i in visited:
        #     print(i)
        # print()
        return visited[n-1][n-1]

    answer = bfs(0,0,0,0)
    answer = min(answer,bfs(0,0,1,0))
    return answer

print(solution([[0,0,0,0,0],[0,1,1,1,0],[0,0,1,0,0],[1,0,0,0,1],[0,1,1,0,0]]))  # 반례(answer:3000, output:3300)
# print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
# print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
# print(solution([[0,0,0],[0,0,0],[0,0,0]]))
# print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))