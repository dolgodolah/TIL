# 처음에 반절만 맞고 반절은 싹 다 틀리길래 뭐가 문제일까.. 생각해봤는데
# 갔던 곳(점)이 아니라 갔던 길(선)을 판별해야했다.
# 갔던 길(선) 판별 여부를 다음과 같이 했다.
# if not (x,y,nx,ny) in visited and not (nx,ny,x,y) in visited:
# 갔던 길 판별 여부와 맵 밖으로 벗어났는지에 따라 게임캐릭터의 위치(queue에 담길 값)이 달라지므로
# if문마다 continue를 통해 구분했다.
from collections import deque
def solution(dirs):
    answer = 0
    queue = deque()
    queue.append((0,0))
    visited = []
    for i in dirs:
        x,y=queue.popleft()
        if i=='U':
            if y+1<=5:
                nx,ny=x,y+1
                if not (x,y,nx,ny) in visited and not (nx,ny,x,y) in visited:
                    visited.append((x,y,nx,ny))
                    visited.append((nx,ny,x,y))
                    queue.append((nx,ny))
                    answer+=1
                    continue
                queue.append((nx,ny))
                continue
            queue.append((x,y))
        elif i=='D':
            if y-1>=-5:
                nx,ny=x,y-1
                if not (x,y,nx,ny) in visited and not (nx,ny,x,y) in visited:
                    visited.append((x,y,nx,ny))
                    visited.append((nx,ny,x,y))
                    queue.append((nx,ny))
                    answer+=1
                    continue
                queue.append((nx,ny))
                continue
            queue.append((x,y))
                
        elif i=='L':
            if x-1>=-5:
                nx,ny=x-1,y
                if not (x,y,nx,ny) in visited and not (nx,ny,x,y) in visited:
                    visited.append((x,y,nx,ny))
                    visited.append((nx,ny,x,y))
                    queue.append((nx,ny))
                    answer+=1
                    continue
                queue.append((nx,ny))
                continue
            queue.append((x,y))
        else:
            if x+1<=5:
                nx,ny=x+1,y
                if not (x,y,nx,ny) in visited and not (nx,ny,x,y) in visited:
                    visited.append((x,y,nx,ny))
                    visited.append((nx,ny,x,y))
                    queue.append((nx,ny))
                    answer+=1
                    continue
                queue.append((nx,ny))
                continue
            queue.append((x,y))
    return answer
print(solution('ULURRDLLU'))