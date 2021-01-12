import sys
input = sys.stdin.readline
n,m,x,y,k = map(int,input().split())
ls = []
for i in range(n):
    ls.append(list(map(int,input().split())))

moves = list(map(int,input().split()))
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
dice = [0,0,0,0,0,0,0]
def move(moves):
    if moves==1: #동
        dice[1],dice[4],dice[6],dice[3]=dice[4],dice[6],dice[3],dice[1]
    elif moves==2: #서
        dice[1],dice[4],dice[6],dice[3]=dice[3],dice[1],dice[4],dice[6]
    elif moves==3: #북
        dice[1],dice[2],dice[6],dice[5]=dice[5],dice[1],dice[2],dice[6]
    elif moves==4: #남
        dice[1],dice[2],dice[6],dice[5]=dice[2],dice[6],dice[5],dice[1]    
def roll(x,y):
    for i in range(k):
        if -1<x+dx[moves[i]]<n and -1<y+dy[moves[i]]<m:
            x+=dx[moves[i]]
            y+=dy[moves[i]]
            move(moves[i])
            if ls[x][y]==0:
                ls[x][y]=dice[6]
            elif ls[x][y]!=0:
                dice[6],ls[x][y]=ls[x][y],0
            print(dice[1])
roll(x,y)