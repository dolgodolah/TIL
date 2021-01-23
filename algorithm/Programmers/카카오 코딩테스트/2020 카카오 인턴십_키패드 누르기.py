# 키패드 1,2,3,4,5,6,7,8,9,0,*,#을 배열의 형태로 정의해주고
# 2,5,8,0(가운데 번호들)을 누를 때 왼손,오른쪽 (x,y) 인덱스를
# dx,dy로 움직여 적게 움직인 손으로 누르게 구현해주면 된다.
from collections import deque
keypad = [[1,2,3]
        ,[4,5,6]
        ,[7,8,9]
        ,['*',0,'#']]
def get_distance(x,y,number):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append((x,y,0))
    visited = [[False]*3 for _ in range(4)]
    visited[x][y]=True
    while queue:
        x,y,cnt=queue.popleft()
        if keypad[x][y]==number:
            return cnt
        for d in range(4):
            if 0<=x+dx[d]<4 and 0<=y+dy[d]<3:
                nx,ny=x+dx[d],y+dy[d]
                if visited[nx][ny]==False:
                    visited[nx][ny]=True
                    queue.append((nx,ny,cnt+1))

def solution(numbers, hand):
    answer = ''
    
    
    left,right='*','#' #현재 왼손, 오른손의 위치
    for number in numbers:
        if number in [1,4,7]: #무조건 왼손
            answer+='L'
            left=number
        elif number in [3,6,9]: #무조건 오른손
            answer+='R'
            right=number
        else: #가운데
            lc,rc=0,0
            #왼손 엄지손가락에서 해당 번호 누르려면 몇 칸 움직여야하는지 구한다.
            for x in range(4):
                for y in range(3):
                    if keypad[x][y]==left:
                        lc=get_distance(x,y,number)
                        break
                if lc!=0:
                    break

            #오른손 엄지손가락에서 해당 번호 누르려면 몇 칸 움직여야하는지 구한다.
            for x in range(4):
                for y in range(3):
                    if keypad[x][y]==right:
                        rc=get_distance(x,y,number)
                        break
                if rc!=0:
                    break
            
            if lc==rc: #똑같이 떨어져 있을 때
                if hand=='right':
                    answer+='R'
                    right=number
                else:
                    answer+='L'
                    left=number
            elif lc>rc: #오른손이 더 가까울 때
                answer+='R'
                right=number
            else:#왼손이 더 가까울때
                answer+='L'
                left=number

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))