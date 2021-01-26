#Given the value of d for m apples and n oranges, 
#determine how many apples and oranges will fall on Sam's house
# (i.e., in the inclusive range [s,t])?

# m개의 사과와 n개의 오렌지들의 d 값이 주어질 때
# 샘의 집[s,t]에 떨어지는 사과와 오렌지들의 수를 구하여라.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple = []
    orange = []
    for i in apples:
        apple.append(a+i)
    for i in oranges:
        orange.append(b+i)
    answer=0
    for i in apple:
        if s<=i<=t:
            answer+=1
    print(answer)
    answer=0
    for i in orange:
        if s<=i<=t:
            answer+=1
    print(answer)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)