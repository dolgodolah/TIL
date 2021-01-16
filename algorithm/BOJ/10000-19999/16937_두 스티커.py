# 주어진 스티커들 중 2개를 골라 붙일 때 붙여진 스티커 넓이의 최댓값을 구하는 문제이다.
# 주어진 스티커들의 가로,세로 길이가 주어지는데 스티커들은 90도 회전할 수 있다. (여기를 잘 구현해야한다.)

# 리스트 sticker의 값을 받을 때 회전했을 때의 값도 넣어줬다.
# 예를 들어 가로세로(2,3)이라면 (3,2)도 같이 넣어줌으로써 스티커1의 경우는 (2,3)과 (3,2)가 있는 것이다.

# 스티커들의 모든 경우에 대해서 for문을 돌린다.
# 두 스티커를 붙였을 때 모눈종이를 벗어나는지 확인해야하는데
# (스티커1 가로길이 + 스티커2 가로길이)가 모눈종이의 가로길이보다 큰지 확인하는 식으로 하면 된다.
# 주의할 점은 두 번째로 붙이는 스티커가 첫 번째로 붙인 스티커의 오른쪽에 붙여지냐 아래쪽에 붙여지냐이다.
# 오른쪽에 붙여진다 해보자. 두 스티커의 가로길이는 (스티커1 가로길이 + 스티커2 가로길이)가 될 것이고
# 세로길이는 스티커1,스티커2의 세로길이 중 더 긴 것이 두 스티커의 세로길이가 될 것이다.
# 이 2가지 경우에 대해서 길이 check를 하고 모눈정이를 벗어나지 않으면 정답 후보(여기서 max값이 정답)가 될 수 있다.

import sys

h, w = map(int,input().split())
n = int(input())
sticker = []
for i in range(n):
    a,b=map(int,input().split())
    sticker.append([(a,b),(b,a)])

answer = 0
for i in range(n-1):
    for j in range(i+1,n):
        for k in range(2):
            for l in range(2):
                #두번째 스티커를 첫번째 스티커 아래 부분에 놓는 경우
                if sticker[i][k][0]+sticker[j][l][0]<=h and max(sticker[i][k][1],sticker[j][l][1])<=w:
                    answer = max(sticker[i][k][0]*sticker[i][k][1]+sticker[j][l][0]*sticker[j][l][1],answer)
                
                #두번째 스티커를 첫번째 스티커 오른쪽 부분에 놓는 경우
                if max(sticker[i][k][0],sticker[j][l][0])<=h and sticker[i][k][1]+sticker[j][l][1]<=w:
                    answer = max(sticker[i][k][0]*sticker[i][k][1]+sticker[j][l][0]*sticker[j][l][1],answer)
print(answer)