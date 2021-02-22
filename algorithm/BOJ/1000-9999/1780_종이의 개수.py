n=int(input())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
answer=[0,0,0]
def cut(x,y,n):
    pivot=board[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if board[i][j]!=pivot:
                cut(x,y,n//3)
                cut(x,y+n//3,n//3)
                cut(x,y+n*2//3,n//3)
                cut(x+n//3,y,n//3)
                cut(x+n//3,y+n//3,n//3)
                cut(x+n//3,y+n*2//3,n//3)
                cut(x+2*n//3,y,n//3)
                cut(x+2*n//3,y+n//3,n//3)
                cut(x+2*n//3,y+2*n//3,n//3)
                return
    if pivot==-1:
        answer[0]+=1
    elif pivot==0:
        answer[1]+=1
    else:
        answer[2]+=1
cut(0,0,n)
for i in answer:
    print(i)