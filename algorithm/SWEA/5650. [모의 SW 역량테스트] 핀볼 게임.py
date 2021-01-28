# 고난과 역경의 과정
# 처음엔 deque를 이용한 bfs풀이를 했다. 방향 전환 처리를 if,elif,else로 했다. -> 시간초과(5개정답)
# 방향 변환 처리를 change배열의 형태에 담아 처리 -> 시간초과(15개정답)
# deque에 넣다뺐다하지않고 현재 좌표 nx,ny만 갱신한다. -> 정답!!

T = int(input())
for t in range(1,T+1):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    change = [
        [],
        [1, 3, 0, 2],
        [3, 0, 1, 2],
        [2, 0, 3, 1],
        [1, 2, 3, 0],
        [1, 0, 3, 2]
    ]
    n=int(input())
    graph=[]
    for _ in range(n):
        graph.append(list(map(int,input().split())))

    #웜홀을 (x,y)에서 발견하면 그 웜홀과 쌍을 이루고 있는 다른 웜홀을 찾아 좌표를 반환한다.
    def find_pair(x,y,num):
        for i in range(n):
            for j in range(n):
                if graph[i][j]==num and (x!=i or y!=j):
                    return i,j
                    
    #해당 좌표(i,j)에서 d방향으로 움직인다.
    def move(i,j,d):
        cnt=0
        nx=i+dx[d]
        ny=j+dy[d]
        while True:
            if 0<=nx<n and 0<=ny<n:
                if (nx,ny)==(i,j) or graph[nx][ny]==-1:
                    return cnt
                elif 1<=graph[nx][ny]<=5:
                    d=change[graph[nx][ny]][d]
                    cnt+=1
                elif 6<=graph[nx][ny]<=10:
                    nx,ny=find_pair(nx,ny,graph[nx][ny])
            else:
                if d==0:
                    d=1
                elif d==1:
                    d=0
                elif d==2:
                    d=3
                else:
                    d=2
                cnt+=1
            nx,ny=nx+dx[d],ny+dy[d]
        
    for i in range(n):
        for j in range(n):
            for d in range(4):
                if graph[i][j]==0:
                    answer=max(answer,move(i,j,d))
    print(f"#{t} {answer}")