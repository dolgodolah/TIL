# 시간초과 때문에 애썼다.
# 처음에는 주어진 날(N)마다 벌집의 모든 칸들을 탐색하여 계산을 해주었다.
# 근데 규칙을 찾아보면 처음 성장하는 가장자리 좌상단부분부터 다 처리해주고 나머지 칸을 처리해주어도
# 나머지 애벌레들은 자신의 왼쪽(L), 왼쪽 위(D), 위쪽(U)의 애벌레들이 다 자란 다음, 그 날 가장 많이 자란 애벌레가 자란 만큼 자신도 자란다. 
# 위 규칙을 배반하지 않는다. 즉, 주어진 날(N)만큼 좌상단부분을 처리해주고
# 나머지 부분은 N만큼이 아닌 (M-1)*(M-1)만큼만 탐색하면 된다.

# 그런데도 시간초과가 떴다. 좌상단 부분을 처리해주는 부분을 잘 구현해야했다.
# x=M-1, y=0으로 초기화하고 if x>0:x-=1 else:y+=1 를 통해 좌표이동을 해주며 연산을 진행한다.

import sys
input=sys.stdin.readline

M,N=map(int,input().split())
hive=[[1]*M for _ in range(M)]
days=[list(map(int,input().split())) for _ in range(N)]
# for i in hive:
#     print(i)
# print(days)



for day in days:
    x=M-1
    y=0
    for _ in range(day[0]):
        if x>0:
            x-=1
        else:
            y+=1
    for _ in range(day[1]):
        if x>0:
            hive[x][y]+=1
            x-=1
        else:
            hive[x][y]+=1
            y+=1
    for _ in range(day[2]):
        if x>0:
            hive[x][y]+=2
            x-=1
        else:
            hive[x][y]+=2
            y+=1

for i in range(1,M):
    for j in range(1,M):
        hive[i][j]=max(hive[i-1][j-1],hive[i-1][j],hive[i][j-1])
    
for i in hive:
    print(*i)