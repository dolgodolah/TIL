# 정수형 배열이 주어졌을 때 그것들의 합을 구하여라.
#!/bin/python3
import os
import sys
#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
