# https://www.acmicpc.net/problem/16917
# 문제를 잘 읽어야 한다. 양념 치킨 최소 X마리, 후라이드 치킨 최소 Y마리이기 때문에
# 실제로 양념치킨을 X+1,X+2...마리 사도 된다. 후라이드도 마찬가지.
# 반반치킨의 수를 기준으로 최소값을 구했다.
# 반반치킨이 0마리일 때는 양념 치킨을 X마리, 후라이드를 Y마리 사야된다.
# 반반치킨이 2마리일 때는 양념 치킨을 X-1마리, 후라이드를 Y-1마리 사야된다.
# 주의할 점은 반반치킨을 max(X,Y)만큼 구매한다는 것이다.
# 그러다보면 구매할 양념치킨의 수=X-α(반반치킨의 수//2)가 음수가 되어버려서 가격과 곱할 때 음수가 나온다.
# 그러니 구매할 치킨의 수가 음수가 되면 0으로 처리한다.

import sys
input = sys.stdin.readline

a,b,c,x,y = map(int,input().split()) #양념가격, 후라이드가격, 반반가격, 

answer = int(10e9)
for i in range(0,max(x,y)*2+1,2): # i는 반반치킨의 수
    if x-i//2<0:
        nx=0
    else:
        nx=x-i//2
    if y-i//2<0:
        ny=0
    else:
        ny=y-i//2
    answer = min(answer,nx*a+ny*b+i*c)
print(answer)
