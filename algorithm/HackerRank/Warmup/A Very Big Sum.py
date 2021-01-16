# In this challenge, you are required to calculate and print the sum of the elements in an array,
# keeping in mind that some of those integers may be quite large.

# 매우 큰 정수들이라는 점을 유의하고, 배열 요수들의 합을 계산하고 출력하자.
# long을 요구하는 문제같은데 파이썬은 int가 long의 범위까지 지원한다.
import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
