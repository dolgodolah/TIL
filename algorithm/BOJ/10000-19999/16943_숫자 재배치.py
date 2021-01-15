# A에 대한 모든 순열에 대해서 아래 조건을 만족시키는 값 중 최댓값을 구해야한다.
# A에 포함된 숫자의 순서를 섞어서 새로운 수 C를 만들려고 할 때
# 가능한 C 중에서 B보다 작으면서, 가장 큰 값을 구해보자. C는 0으로 시작하면 안 된다.
# 순열을 구할 때는 str형으로 취급해주고, 위 조건에 대해 참거짓을 판단할 때는 int형으로 취급해준다.

import sys
from itertools import permutations

def check(ls):
    if ls[0]=='0':
        return False
    num = int(''.join(ls))
    if num<=int(b):
        return True
    return False
a,b = map(str,input().split())
a = list(a)
answer = -1
for i in permutations(a,len(a)):
    if check(i):
        answer=max(answer,int(''.join(i)))
print(answer)