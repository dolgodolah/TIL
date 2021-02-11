# 로봇이 좌표값 두개를 차지하고 있어 좌표이동을 항상 두개씩 생각해야한다.
# 상하좌우 이동은 비교적 쉬운편인데 90도 회전을 구현하는데 조건이 까다로운 편이다.

# 1.회전하기 위해서는 해당 칸뿐만이 아니라 회전하는데 거치는 칸도 빈칸(0)이어야 한다.
# 2.로봇이 가로로 있을때와 세로로 있을때와 연산을 다르게 해줘야한다.
# 3.시계방향으로 회전, 반시계방향으로 회전 둘 다 구현해줘야한다.

# 방문처리하는 visited도 처음에는 빈 리스트에 방문할때마다 추가해줬는데
# 이러면 방문여부를 확인하는데 시간이 오래걸려 시간초과가 발생한다.
# set으로 설정해서 시간초과를 해결했다. (set은 hash테이블로 구현돼있다고 한다.)

from collections import deque
move = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(board):
    n = len(board)
    queue = deque()
    
    queue.append(((0,0),(0,1),0))
    visited = set()
    visited.add(((0,0),(0,1)))
    # print(queue)
    # print(visited)
    while queue:
        robot1, robot2, cnt = queue.popleft()
        # print(robot1,robot2)
        if robot1==(n-1,n-1) or robot2==(n-1,n-1):
            return cnt
        for dx,dy in move:
            nr1 = (robot1[0]+dx,robot1[1]+dy)
            nr2 = (robot2[0]+dx,robot2[1]+dy)
            if 0<=nr1[0]<n and 0<=nr1[1]<n and 0<=nr2[0]<n and 0<=nr2[1]<n:
                if board[nr1[0]][nr1[1]]==0 and board[nr2[0]][nr2[1]]==0:
                    if not (nr1,nr2) in visited:
                        queue.append((nr1,nr2,cnt+1))
                        visited.add((nr1,nr2))

        if robot1[0]==robot2[0]: #로봇이 가로방향으로 있을 때
            for d in [-1,1]:
                if 0<=robot1[0]+d<n and 0<=robot2[0]+d<n:
                    if board[robot1[0]+d][robot1[1]]==0 and board[robot2[0]+d][robot2[1]]==0:
                        if not (robot1,(robot1[0]+d,robot1[1])) in visited:
                            queue.append((robot1,(robot1[0]+d,robot1[1]),cnt+1))
                            visited.add((robot1,(robot1[0]+d,robot1[1])))
                        if not ((robot2[0]+d,robot2[1]),robot2) in visited: 
                            queue.append(((robot2[0]+d,robot2[1]),robot2,cnt+1))
                            visited.add(((robot2[0]+d,robot2[1]),robot2))

        elif robot1[1]==robot2[1]: #로봇이 세로방향으로 있을 때
            for d in [-1,1]:
                if 0<=robot1[1]+d<n and 0<=robot2[1]+d<n:
                    if board[robot1[0]][robot1[1]+d]==0 and board[robot2[0]][robot2[1]+d]==0:
                        if not (robot1,(robot1[0],robot1[1]+d)) in visited:
                            queue.append((robot1,(robot1[0],robot1[1]+d),cnt+1))
                            visited.add((robot1,(robot1[0],robot1[1]+d)))
                        if not ((robot2[0],robot2[1]+d),robot2) in visited:
                            queue.append(((robot2[0],robot2[1]+d),robot2,cnt+1))
                            visited.add(((robot2[0],robot2[1]+d),robot2))

            
def solution(board):
    answer = 0
    answer = bfs(board)
    return answer


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))