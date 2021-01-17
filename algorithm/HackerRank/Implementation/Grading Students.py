#모든 학생은 0~100점 사이의 성적은 받는다.
#교수 sam은 다음 규칙에 따라 학생들의 성적을 반올림하는 걸 좋아한다.

#해당 학생 성적이 다음 5의 배수와 차이가 3보다 작으면 다음 5의 배수로 반올림 해준다. ex) 83,84->85
#해당 학생 성적이 38점보다 적으면 반올림 하지않는다. 
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i]>=38 and grades[i]%5>=3:
            grades[i]+=5-grades[i]%5
    
    return grades
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
