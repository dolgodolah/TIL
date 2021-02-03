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