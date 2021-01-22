#매직 스퀘어로 변경되기 위한 조건이 뭐가 있을까 1시간동안 고민했다.
#결론은 다 해보는거다. n*n 크기의 배열이라길래 n이 조금만 커져도 말이 안되는 범위다.
#근데 3x3이란다. 문제 예시만 3x3인줄 알았다. 근데 전부 다 3x3이다.
#permutations로 가능한 3x3 배열을 구하고
#3x3 배열 중 하나인 [[1,2,3],[2,3,4],[5,6,7]]를 예로들어보자.
#[[1,2,3],[2,3,4],[5,6,7]]가 매직스퀘어인지 check()를 통해 확인하고
#True라면 입력으로 주어진 배열과 [[1,2,3],[2,3,4],[5,6,7]]의 차이를 calc()한다.
#calc한 값이 최솟값이라면 갱신해준다.

#고려해줄 부분은 2차원 배열을 1차원 배열로 바꿔 생각하는 부분이다.
import sys
from itertools import permutations
input = sys.stdin.readline

def check(ls):
    val = sum(ls[0:3])#기준

    #가로 검사
    for i in range(0,9,3):
        if sum(ls[i:i+3])!=val:
            return False

    #세로 검사
    for i in range(3):
        if val!=ls[i]+ls[i+3]+ls[i+6]:
            return False
    
    #대각선 검사
    sum_v=0
    if ls[0]+ls[4]+ls[8]!=val:
        return False
    if ls[2]+ls[4]+ls[6]!=val:
        return False

    return True

def calc(ls):
    result=0
    for i in range(3):
        for j in range(3):
            result+=abs(graph[i][j]-ls[i*3+j])
    return result
graph=[]
for _ in range(3):
    graph.append(list(map(int,input().split())))

answer = int(10e9)
for i in permutations(range(1,10),9):
    if check(i):
        answer=min(answer,calc(i))
print(answer)