# 입력이 종료될때까지 받는 문제라 eof를 알아야된다. 파이썬에서는 try, except로 해결했다.
# 미리 입력으로 주어진 맵의 칸 수(벽 제외)를 total에 저장하고,
# 백트래킹에서 지나간 칸의 수(cnt)가 total과 같아졌을 때 정답을 갱신한다.

# 해당 direction으로 쭉 이동시키다가 맵밖을 벗어나거나 이미 방문했거나 벽에 부딪히면
# direction을 바꿔서 위 조건을 다시 판단해본다. direction을 다 바꿔봤는데도 안되면 dfs는 종료된다.

def dfs(x,y,direction,cnt,result):
    global answer
    if cnt==total: #지나간 칸의 수가 '.'의 수와 일치하면 종료
        answer = min(answer,result)

    nx = x+dx[direction]
    ny = y+dy[direction]

    if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False and graph[nx][ny]=='.':
        visited[nx][ny]=True
        dfs(nx,ny,direction,cnt+1,result)
        visited[nx][ny]=False
    else:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False and graph[nx][ny]=='.':
                visited[nx][ny]=True
                dfs(nx,ny,i,cnt+1,result+1)
                visited[nx][ny]=False

            
dx = [-1,1,0,0]
dy = [0,0,-1,1]
case = 1
while True:
    try:
        n,m=map(int,input().split())
        graph=[]
        visited = [[False]*m for _ in range(n)]
        for _ in range(n):
            graph.append(list(input()))
        
        total=0 #이동해야하는 칸의 총 개수
        for i in range(n):
            for j in range(m):
                if graph[i][j]=='.':
                    total+=1
        if total==1:
            print(f"Case {case}: 0")
        else:
            answer = int(10e9)
            for i in range(n):
                for j in range(m):
                    if graph[i][j]=='.':
                        for k in range(4):
                            visited[i][j]=True
                            dfs(i,j,k,1,1)
                            visited[i][j]=False
            if answer==int(10e9):
                print(f"Case {case}: -1")
            else:
                print(f"Case {case}: {answer}")
        case+=1
    except:
        break