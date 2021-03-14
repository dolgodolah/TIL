# dfs를 통해 격자판을 달팽이 모양으로 순회하였다.
# 격자를 벗어나거나 이미 방문했던 곳이면 direction을 오른쪽,아래,왼쪽,위 순서대로 이동하도록 바꿔준다.

test_case=int(input())
for t in range(1,test_case+1):
    n=int(input())
    array=[[0]*n for _ in range(n)]
    direction=0
    move=[(0,1),(1,0),(0,-1),(-1,0)] #오른쪽, 아래, 왼쪽, 위
    def dfs(x,y,direction,cnt):
        nx=x+move[direction][0]
        ny=y+move[direction][1]
        if cnt>n**2:
            return
        if 0<=nx<n and 0<=ny<n and array[nx][ny]==0:
            array[nx][ny]=cnt
            dfs(nx,ny,direction,cnt+1)
        else:
            dfs(x,y,(direction+1)%4,cnt)

    dfs(0,-1,0,1)
    print(f"#{t}")
    for i in array:
        print(*i)
        
        