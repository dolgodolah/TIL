# L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
# R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.

# 첫번째 시도(시간초과) : 위 두 명령어에 대한 처리를 .zfill(4)와 pop(), append(), insert()를 이용해 처리했다
# 두번째 시도(4200ms) : 위 두 명령어에 대한 처리를 수학적 계산으로 처리했다.
# L에 대한 처리는 가장 왼쪽 숫자를 추출(n//1000)하고 나머지 오른쪽 세 숫자(n%1000)의 오른쪽에 0을 추가하고(*10)한 수에 아까 추출했던 숫자를 더 해준다.
# num3=n%1000*10+n//1000 

# R에 대한 처리는 가장 오른쪽 숫자를 추출(n%10)하고 나머지 왼쪽 세 숫자(n//10)의 왼쪽에 붙이려면 추출한 숫자에 *1000을 해주고 더해준다.
# num4=n%10*1000+n//10


import sys
from collections import deque
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    a,b=map(int,input().split())
    visited=[int(10e9)]*10000
    visited[a]=0
    queue=deque()
    queue.append((a,''))
    while queue:
        n,command=queue.popleft()
        if n==b:
            print(command)
            break

        value=len(command)+1
        num1=(n*2)%10000
        if visited[num1]>value:
            visited[num1]=value
            queue.append((num1,command+'D'))
        
        num2=n-1 if n!=0 else 9999
        if visited[num2]>value:
            visited[num2]=value
            queue.append((num2,command+'S'))

        num3=n%1000*10+n//1000
        if visited[num3]>value:
            visited[num3]=value
            queue.append((num3,command+'L'))

        num4=n%10*1000+n//10
        if visited[num4]>value:
            visited[num4]=value
            queue.append((num4,command+'R'))
