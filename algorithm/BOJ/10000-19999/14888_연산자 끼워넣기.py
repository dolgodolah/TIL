import sys
from itertools import permutations
input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))
temp = list(map(int,input().split()))
operators = []
for i in range(len(temp)):
    for _ in range(temp[i]):
        if i==0:
            operators.append('+')
        elif i==1:
            operators.append('-')
        elif i==2:
            operators.append('*')
        elif i==3:
            operators.append('/')
def calc(nums,operators):
    num1 = nums[0]
    for i in range(1,n):
        if operators[i-1]=='+':
            num1 += nums[i]
        elif operators[i-1]=='-':
            num1 -= nums[i]
        elif operators[i-1]=='*':
            num1 *= nums[i]
        elif operators[i-1]=='/':
            if num1<0:
                num1 = -1*((-1*num1)//nums[i])
            else:
                num1 = num1//nums[i]
    return num1
sub_answer = []
for i in permutations(operators,n-1):
    i = list(i)
    sub_answer.append(calc(nums,i))
print(max(sub_answer))
print(min(sub_answer))
