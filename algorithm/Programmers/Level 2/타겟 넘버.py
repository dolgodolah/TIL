# 21년 5월 5일 두번째 풀이
from collections import deque
def solution(numbers, target):
    answer = 0
    queue=deque()
    queue.append((0,0))
    while queue:
        x,cnt=queue.popleft()
        # print(x,cnt)
        if cnt==len(numbers) and x==target:
            answer+=1
        if cnt+1<=len(numbers):
            queue.append((x+numbers[cnt],cnt+1))
            queue.append((x-numbers[cnt],cnt+1))
    return answer

print(solution([1,1,1,1,1],3))


# 21년 1월 25일 첫번째 풀이
answer = 0
def dfs(cnt,result,numbers,target):
    global answer
    if cnt==len(numbers):
        if result==target:
            answer+=1
        return
        
    dfs(cnt+1,result+numbers[cnt],numbers,target)
    dfs(cnt+1,result-numbers[cnt],numbers,target)

def solution(numbers, target):
    global answer
    dfs(0,0,numbers,target)
    return answer

print(solution([1, 1, 1, 1, 1],3))