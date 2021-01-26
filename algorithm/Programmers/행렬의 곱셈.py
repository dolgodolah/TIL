#numpy.array() -> 리스트를 행렬로 변환
#numpy.dot() -> 행렬곱
import numpy as np

def solution(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    answer=np.dot(arr1,arr2).tolist()
    return answer

print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]]))