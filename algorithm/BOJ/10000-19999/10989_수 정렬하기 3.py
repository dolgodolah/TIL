# 같은 풀이로 python은 통과, pypy3는 메모리초과이다.
# sys.stdin.readline을 사용하지 않으면 python으로도 안된다.

import sys
input = sys.stdin.readline
n=int(input())
ls = [0]*10001
for _ in range(n):
    ls[int(input())]+=1

for i in range(1,10001):
    for _ in range(ls[i]):
        print(i)