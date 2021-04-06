import sys
input=sys.stdin.readline
H,W,X,Y=map(int,input().split())
B=list()
for _ in range(X+H):
    B.append(list(map(int,input().split())))

A=[[0]*(W+Y) for _ in range(H+X)]
visited=[[0]*(Y+W) for _ in range(X+H)]


for i in range(H):
    for j in range(W):
        visited[i][j]+=1
for i in range(X,X+H):
    for j in range(Y,Y+W):
        visited[i][j]+=1

# for i in visited:
#     print(i)
# print()

for i in range(H+X):
    for j in range(W+Y):
        if visited[i][j]==2:
            A[i][j]=B[i][j]-A[i-X][j-Y]
        elif visited[i][j]==1:
            A[i][j]=B[i][j]

for i in range(H):
    for j in range(W):
        print(A[i][j],end=" ")
    print()

            
