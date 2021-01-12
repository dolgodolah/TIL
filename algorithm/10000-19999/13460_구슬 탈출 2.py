from collections import deque
import sys
input = sys.stdin.readline
n,m=map(int,input().split())
graph = []
move_type = [(-1,0),(1,0),(0,-1),(0,1)]
for _ in range(n):
    graph.append(list(map(str,input())))

def move(x,y,dx,dy):
    move_range=0
    #벽에 부딪히거나 구멍에 빠질때까지 움직인다.
    while graph[x+dx][y+dy]!='#' and graph[x][y]!='O':
        x,y = x+dx,y+dy
        move_range+=1
    return x,y,move_range

def bfs(ri,rj,bi,bj):
    visited = []
    queue = deque()
    queue.append([ri,rj,bi,bj,1])
    visited.append([ri,rj,bi,bj])
    while queue:
        rx,ry,bx,by,count = queue.popleft() #빨간구슬좌표, 파란구슬좌표, 움직인횟수
        if count>10: #움직인횟수가 10번 넘으면 -1 출력
            return -1
        for dx,dy in move_type:
            nrx,nry,rmove_range=move(rx,ry,dx,dy)
            nbx,nby,bmove_range=move(bx,by,dx,dy)
          
            # 파란구슬이 구멍에 빠진 경우는 무시
            # if graph[bx][by]=='O': 
            #     continue 

            if graph[nbx][nby]!='O': 
                if graph[nrx][nry]=='O': #빨간구슬만 구멍에 빠지면 성공
                    return count
                if nrx==nbx and nry==nby: #빨간구슬과 파란구슬의 위치가 같으면
                    #이동거리가 더 긴 구슬이 한 칸 뒤로 간다.
                    if rmove_range>bmove_range: 
                        nrx-=dx
                        nry-=dy
                    elif rmove_range<bmove_range:
                        nbx-=dx
                        nby-=dy
                if not [nrx,nry,nbx,nby]  in visited:
                    visited.append([nrx,nry,nbx,nby])
                    queue.append([nrx,nry,nbx,nby,count+1])
    return -1 #빨간구슬이 먼저 구멍에 빠지는 경우가 없다.
                
#구슬들의 위치를 찾는다.
for i in range(n):
    for j in range(m):
        if graph[i][j]=='R':
            red_i,red_j = i,j
        if graph[i][j]=='B':
            blue_i,blue_j = i,j

print(bfs(red_i,red_j,blue_i,blue_j))
