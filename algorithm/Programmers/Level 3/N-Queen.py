from collections import deque
answer = 0

def dfs(x,y,diag,diag2,n):
    global answer
    if x==n:
        # for i in board:
        #     print(i)
        # print()
        answer+=1
        return
    for i in range(n):
        if y[i]==0 and diag[x+i]==0 and diag2[i-x]==0:
            y[i],diag[x+i],diag2[i-x]=1,1,1
            dfs(x+1,y,diag,diag2,n)
            y[i],diag[x+i],diag2[i-x]=0,0,0

def solution(n):
    global answer
    answer = 0
    y = [0]*n
    diag = [0]*(2*n-1)
    diag2 = [0]*(2*n-1)
    dfs(0,y,diag,diag2,n)

    return answer

print(solution(4))