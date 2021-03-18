# 배열의 회전은 이미 알고있어 쉬웠는데 출력형식이 까다로워 시간이 걸렸다.
# (7,4,1) -> '741'와 같이 튜플을 문자열로 반환하려면 ''.join((7,4,1))을 해야한다.
# join을 하기 위해서는 튜플안에 있는 원소들이 str형이어야하는데 배열을 입력받을 때 int형으로 받아서 자꾸 에러가 떴다.
# 배열을 입력받을 때 str으로 바꿔주니 바로 해결됐다.

T=int(input())
for t in range(1,T+1):
    n=int(input())
    board=[list(map(str,input().split())) for _ in range(n)]
    answer=[[] for _ in range(3)]
    for i in range(3):
        board=list(zip(*board[::-1]))
        for j in board:
            answer[i].append(''.join(j))
    print(f"#{t}")
    for i in range(n):
        for j in range(len(answer)):
            print(answer[j][i],end=" ")
        print()
