# The first kangaroo starts at location X1 and moves at a rate of V1 meters per jump.
# The second kangaroo starts at location X2 and moves at a rate of V2 meters per jump.
# 첫번째 캥거루는 X1에서부터 V1의 속도로 움직이고
# 두번째 캥거루는 X2에서부터 V2의 속도로 움직인다.

# You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. 
# If it is possible, return YES, otherwise return NO.
# 두 캥거루가 동시에 같은 지점에 있을 수 있는지 알아내라
# 가능하다면 YES를, 아니면 NO를 반환해라.



x1,v1,x2,v2=map(int,input().split())
answer = 0
if v1<=v2:
    print("NO")
else:
    while x1<x2:
        x1+=v1
        x2+=v2
    if x1==x2:
        print("YES")
    else:
        print("NO")