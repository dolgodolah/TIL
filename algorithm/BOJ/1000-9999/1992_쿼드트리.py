n=int(input())
board=list()
for _ in range(n):
    board.append(list(map(int,input())))
answer=[]
def cut(x,y,n):
    tmp=board[x][y]
    
    for i in range(x,x+n):
        for j in range(y,y+n):
            if board[i][j]!=tmp:
                answer.append("(")
                cut(x,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y,n//2)
                cut(x+n//2,y+n//2,n//2)
                answer.append(")")
                return
    
    if board[x][y]==0:
        answer.append('0')
    else:
        answer.append('1')
cut(0,0,n)
print(''.join(answer))