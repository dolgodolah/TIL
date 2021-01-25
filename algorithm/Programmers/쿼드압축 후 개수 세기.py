# def solution(arr):
#     answer = [0,0]
#     n = len(arr)
#     def dfs(x,y,n):
#         temp = arr[x][y]
#         for i in range(x,x+n):
#             for j in range(y,y+n):
#                 if arr[i][j]!=temp:
#                     nn = n//2
#                     dfs(x,y,nn)
#                     dfs(x,y+nn,nn)
#                     dfs(x+nn,y,nn)
#                     dfs(x+nn,y+nn,nn)
#                     return
#         answer[temp]+=1
#     dfs(0,0,n)
#     return answer





def solution(arr):
    answer = [0,0]

    def dfs(x,y,n):
        temp = arr[x][y]
        for i in range(x,x+n):
            for j in range(y,y+n):
                if arr[i][j]!=temp:
                    nn = n//2
                    dfs(x,y,nn)
                    dfs(x,y+nn,nn)
                    dfs(x+nn,y,nn)
                    dfs(x+nn,y+nn,nn)
                    return
        answer[temp]+=1  
    dfs(0,0,len(arr))
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))