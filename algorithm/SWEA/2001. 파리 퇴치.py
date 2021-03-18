#파리채 크기 m*m이 맵(n*n) 밖을 벗어났을 때는 catch()를 하지 않아도 된다. 

T=int(input())
for t in range(1,T+1):
    n,m=map(int,input().split())
    board=[list(map(int,input().split())) for _ in range(n)]

    def catch(x,y):
        result=0
        for i in range(x,x+m):
            for j in range(y,y+m):
                result+=board[i][j]
        return result

    answer=0
    for i in range(n-m+1):
        for j in range(n-m+1):
            answer=max(answer,catch(i,j))
    
    print(f"#{t} {answer}")
                
