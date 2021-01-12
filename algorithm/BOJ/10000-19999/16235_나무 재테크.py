import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int,input().split())
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
graph = [[5]*n for _ in range(n)]
s2d2 = []
tree = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(n):
    s2d2.append(list(map(int,input().split())))
for _ in range(m):
    a,b,c=map(int,input().split())
    tree[a-1][b-1].append(c)


for i in range(n):
    for j in range(n):
        if tree[i][j]:
            tree[i][j].sort()
        tree[i][j]=deque(tree[i][j])

def springAndSummer():
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                deadtree = 0
                for _ in range(len(tree[i][j])):
                    age = tree[i][j].popleft()
                    # 양분 부족해서 죽음
                    if age>graph[i][j]:
                        deadtree += age//2
                    # 양분 먹고 나이 증가
                    else:
                        graph[i][j]-=age
                        age+=1
                        tree[i][j].append(age)
                graph[i][j]+=deadtree
                
def fall():
    for x in range(n):
        for y in range(n):
            if tree[x][y]:
                for age in tree[x][y]:
                    if age%5==0:
                        for i in range(8):
                            if 0<=x+dx[i]<n and 0<=y+dy[i]<n:
                                tree[x+dx[i]][y+dy[i]].appendleft(1)

def winter():
    for i in range(n):
        for j in range(n):
            graph[i][j]+=s2d2[i][j]
                        

for _ in range(k):
    springAndSummer()
    fall()
    winter()
answer=0
for i in range(n):
    for j in range(n):
        if tree[i][j]:
            answer+=len(tree[i][j])
print(answer)
# for i in tree:
#     print(i)
