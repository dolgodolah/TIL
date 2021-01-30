# 백준에서 풀었던 경사로 문제와 동일하다.
# 나름 PS 많이 해봤다고 생각했는데 다시 푸는건데도 불구하고 너무 오래 걸렸다.
# 반복문을 돌리는데 조건에 따라 break, continue를 적절히 사용해야하고 idx 처리하는데도 생각을 많이 해야했다.
# 가장 골치아팠던건 해당 칸이 전보다 높아졌느냐 낮아졌느냐에 따라 idx를 처리하는 방법이 다른것이다.


T=int(input())
for t in range(1,T+1):
    n,x=map(int,input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int,input().split())))
    answer = 0

    #가로 방향 검사
    for i in range(n):
        cnt=1 #해당 높이가 지속된 횟수를 나타낸다. 높은 땅이 나타났을 때 cnt가 x만큼 충분히 있어야 경사로 설치 가능하다.
        idx=1
        while idx<n:
            if board[i][idx]==board[i][idx-1]: #해당 높이가 지속되면 cnt+1 해준다.
                cnt+=1
            elif board[i][idx]==board[i][idx-1]+1:#해당 칸이 전보다 높을 때
                if cnt<x: #경사로를 설치하기에 cnt가 부족하면 해당 i에서는 활주로 설치 불가능하다.
                    break
                cnt=1 #경사로가 설치가능하다면 다시 해당 높이 지속 횟수를 나타내는 cnt를 1로 초기화해준다.

            elif board[i][idx]==board[i][idx-1]-1:#해당 칸이 전보다 낮을 때
                if board[i][idx:idx+x].count(board[i][idx])<x: #해당칸부터 경사로의 길이만큼에서 동일높이 칸이 부족하다면 설치 불가능
                    break
                idx+=x #설치가능하다면 경사로의 길이만큼 더해준다. (경사로를 설치한 칸은 볼 필요가 없으므로)
                cnt=0 #여기가 중요하다. cnt는 해당 높이의 지속 횟수이므로 0으로 초기화 해줘야한다.
                continue
            else:
                break
            idx+=1

        if idx==n: #경사로 설치 가능!
            answer+=1


    #세로 방향 검사
    for i in range(n):
        cnt=1
        idx=1
        while idx<n:
            if board[idx][i]==board[idx-1][i]:
                cnt+=1
            elif board[idx][i]==board[idx-1][i]+1:#해당 칸이 전보다 높으면
                if cnt<x:
                    break
                cnt=1
            elif board[idx][i]==board[idx-1][i]-1:#해당 칸이 전보다 낮으면
                tmp_cnt=0
                for k in range(idx,idx+x):
                    if k<n and board[k][i]==board[idx][i]:
                        tmp_cnt+=1
                    else:
                        break
                if tmp_cnt<x:
                    break
                idx+=x
                cnt=0
                continue
            else:
                break
            idx+=1
        if idx==n: #경사로 설치 가능!
            answer+=1
    print(f"#{t} {answer}")