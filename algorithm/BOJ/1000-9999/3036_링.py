# 파이썬에 내장돼있는 기본 라이브러리 fractions의 Fraction을 배웠다.
# 실수를 기약분수 형태로 나타낸다.

from fractions import Fraction
n=int(input())
ring=list(map(int,input().split()))
for i in range(1,n):
    num = Fraction(ring[0],ring[i])
    if ring[0]%ring[i]==0:
        print(str(num)+"/"+'1')
    else:
        print(num)
