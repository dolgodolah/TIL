T=int(input())
for t in range(1,T+1):
    board=[list(map(int,input().split())) for _ in range(9)]

    def row_check(i):
        visited=[False]*10
        for j in range(9):
            if visited[board[i][j]]==False:
                visited[board[i][j]]=True
            else:
                print("TEST")
                return False
        return True

    def column_check(i):
        visited=[False]*10
        for j in range(9):
            if visited[board[j][i]]==False:
                visited[board[j][i]]=True
            else:
                print("TEST")
                return False
        return True

    def squre_check():
        for i in range(3):
            for j in range(3):
                visited=[False]*10
                for k in range(3*i,3*i+3):
                    for l in range(3*j,3*j+3):
                        if visited[board[k][l]]==False:
                            visited[board[k][l]]=True
                        else:
                            print("TST")
                            return False
        return True

    answer=1
    for i in range(9):
        if row_check(i)==False:
            answer=0
        if column_check(i)==False:
            answer=0

    if squre_check()==False:
        answer=0

    print(answer)