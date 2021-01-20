def checkBasket(basket):
    if len(basket)<2: #인형이 1개거나 없을 때는 점수 계산 x
        return 0
    if basket[len(basket)-1]==basket[len(basket)-2]: #점수 획득
        basket.pop()
        basket.pop()
        return 2
    else:
        return 0

def solution(board, moves):
    answer = 0
    basket = []
    for move in moves:
        for i in range(len(board)): #위에서 아래로 탐색하는데
            if not board[i][move-1]==0: #인형 최초 발견하면
                basket.append(board[i][move-1]) #바구니에 인형 쌓는다.
                board[i][move-1]=0 #해당 칸은 빈 칸이 된다.
                break
        answer+=checkBasket(basket) #바구니를 확인해서 반환되는 점수를 더해준다.
    return answer


# [[0,0,0,0,0],
#  [0,0,1,0,3],
#  [0,2,5,0,1],
#  [4,2,4,4,2],
#  [3,5,1,3,1]]

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))