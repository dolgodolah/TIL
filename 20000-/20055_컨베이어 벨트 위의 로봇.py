import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())
A = deque(list(map(int,input().split())))
visited = deque([False]*n)
answer = 0

# 4. 내구도가 0인 칸의 개수가 k개 이상이면 종료
while A.count(0)<k:
    answer+=1

    # 1. 벨트 한 칸 회전
    if visited[n-1]==True: # 내려가는 위치에 로봇있으면 
        visited[n-1]=False # 로봇 제거
    A.appendleft(A.pop()) #회전
    visited.appendleft(visited.pop())

    # 2. 로봇 이동
    for i in range(n-1,-1,-1): 
        if i == n-1:
            if visited[i]==True: # 내려가는 위치에 로봇있으면
                visited[i]=False # 로봇 제거
        elif visited[i]==True and visited[i+1]==False and A[i+1]>=1: #앞으로 이동할 수 있다면 이동
            visited[i],visited[i+1]=False,True
            A[i+1]-=1
            
    if visited[0]==False and A[0]>=1: #3 올라가는 위치에 로봇 없으면 로봇 추가
        visited[0]=True
        A[0]-=1
print(answer)