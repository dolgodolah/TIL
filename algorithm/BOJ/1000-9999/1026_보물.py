import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
# 문제에서 A 리스트만 재배치가 가능하다 했는데
# 재배치를 통해 문제에서 요구하는 연산의 최소값은 결국
# A에서 가장 큰 값 x B에서 가장 작은 값을 순서대로 곱하는거다.
A.sort(reverse=True)
B.sort()
answer = 0
for i in range(n):
    answer += A[i]*B[i]
print(answer)

# def calc(A):
#     _sum = 0
#     for i in range(n):
#         _sum += A[i]*B[i]
#     return _sum

# answer = int(10e9)
# for i in permutations(A,n):
#     answer = min(answer,calc(i))
# print(answer)