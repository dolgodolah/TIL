# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with 6 places after the decimal.
# 정수들의 배열 주어졌을 때 양수,음수,0인 요소들의 비율을 계산해라.
# 소수점 아래 6자리까지 구하여라
# fraction 분수, decimal 소수

#!/bin/python3

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    positive, negative, zero = 0,0,0
    for i in arr:
        if i>0:
            positive+=1
        elif i<0:
            negative+=1
        else:
            zero+=1
    print('%.6f'%positive/len(arr))        
    print('%.6f'%negative/len(arr))
    print('%.6f'%zero/len(arr))
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
