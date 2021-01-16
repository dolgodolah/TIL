# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix  is shown below:

# 정사각행렬 주어졌을 때 두 대각선의 합 차이를 계산하자.
# diagonal 대각선
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    sum1,sum2=0,0
    for i in range(len(arr)):
        sum1+=arr[i][i]
        sum2+=arr[i][len(arr)-1-i]
    return abs(sum1-sum2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
