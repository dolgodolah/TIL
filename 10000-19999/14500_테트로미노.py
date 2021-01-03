import sys

input = sys.stdin.readline
tetrominos1=[[(0,0),(0,1),(0,2),(0,3)]
            ,[(0,0),(1,0),(2,0),(3,0)]]

tetrominos2=[[(0,0),(1,0),(0,1),(1,1)]]

tetrominos3=[[(0,0),(1,0),(2,0),(2,1)]
            ,[(0,0),(0,1),(0,2),(1,0)]
            ,[(0,0),(0,1),(1,1),(2,1)]
            ,[(0,2),(1,0),(1,1),(1,2)]
            ,[(0,0),(0,1),(1,0),(2,0)]
            ,[(0,0),(0,1),(0,2),(1,2)]
            ,[(0,0),(1,0),(1,1),(1,2)]
            ,[(0,1),(1,1),(2,1),(2,0)]]

tetrominos4=[[(0,0),(1,0),(1,1),(2,1)]
            ,[(1,0),(1,1),(0,1),(0,2)]
            ,[(0,1),(1,1),(1,0),(2,0)]
            ,[(0,0),(0,1),(1,1),(1,2)]]

tetrominos5=[[(0,0),(0,1),(0,2),(1,1)]
            ,[(1,0),(0,1),(1,1),(2,1)]
            ,[(1,0),(1,1),(0,1),(1,2)]
            ,[(0,0),(1,0),(1,1),(2,0)]]

n,m=map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

def get_max(idx):
    sub_answer = 0
    if idx == 0:
        for i in range(n):
            for j in range(m):
                for move in tetrominos1:
                    temp = 0
                    for x,y in move:
                        if -1<i+x<n and -1<j+y<m :
                            temp+=graph[i+x][j+y]
                        else:
                            break
                    sub_answer = max(temp,sub_answer)

    elif idx == 1:
        for i in range(n):
            for j in range(m):
                for move in tetrominos2:
                    temp = 0
                    for x,y in move:
                        if -1<i+x<n and -1<j+y<m :
                            temp+=graph[i+x][j+y]
                        else:
                            break
                    sub_answer = max(temp,sub_answer)
    elif idx == 2:
        for i in range(n):
            for j in range(m):
                for move in tetrominos3:
                    temp = 0
                    for x,y in move:
                        if -1<i+x<n and -1<j+y<m :
                            temp+=graph[i+x][j+y]
                        else:
                            break
                    sub_answer = max(temp,sub_answer)
    elif idx == 3:
        for i in range(n):
            for j in range(m):
                for move in tetrominos4:
                    temp = 0
                    for x,y in move:
                        if -1<i+x<n and -1<j+y<m :
                            temp+=graph[i+x][j+y]
                        else:
                            break
                    sub_answer = max(temp,sub_answer)
    elif idx == 4:
        for i in range(n):
            for j in range(m):
                for move in tetrominos5:
                    temp = 0
                    for x,y in move:
                        if -1<i+x<n and -1<j+y<m :
                            temp+=graph[i+x][j+y]
                        else:
                            break
                    sub_answer = max(temp,sub_answer)
    return sub_answer
answer = 0
for i in range(5):
    answer = max(answer, get_max(i))
print(answer)