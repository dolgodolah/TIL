n=int(input())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
w,b=0,0
def solution(x,y,n):
    global w,b
    color = board[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color!=board[i][j]:
                solution(x,y,n//2)
                solution(x+n//2,y,n//2)
                solution(x,y+n//2,n//2)
                solution(x+n//2,y+n//2,n//2)
                return

    if color==0:
        w+=1
    else:
        b+=1

solution(0,0,n)
print(w)
print(b)