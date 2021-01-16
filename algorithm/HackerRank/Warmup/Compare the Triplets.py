# alice와 bob이 각자 문제를 만들고, 평가자가 이 문제에 대해 평가를 내린다.
# 3항목으로 1~100사이의 점수를 준다.
# alice 문제의 3항목 점수는 a=(a[0],a[1],a[2]) 형식으로 주어진다.
# alice와 bob의 3항목 점수를 비교해서 높으면 1점 획득한다. 비기면 0
# 각자 얻은 점수를 반환하자.

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
