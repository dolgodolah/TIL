# 첫번째 시도(시간초과) : itertools의 combinations을 이용했다.
# 두번째 시도(런타임에러) : 문제들과 answer을 탐색하며 문제를 맞춘 경우와 맞추지 못한 경우를 answer에 누적시켰다.

# 두번째 시도에서 생각했던 풀이방법을 제대로 구현하지 못했다.
# 정답 풀이를 보니 answer을 set으로 만들어 | 연산을 사용하였다.
# set들끼리는 |와 &연산이 가능하다는 걸 배웠다.

# 예를 들어 2,3,5점짜리 문제들이 있고 answer에는 아무 문제도 맞추지 못한 0점이 추가돼있다고 하자. answer={0}
# 문제들과 answer를 탐색하며 answer에 구해진 점수들을 추가한다.
# 0+2점이 만들어질 수 있고 answer={0,2}가 된다. 그 다음 문제를 탐색할 때는 0+3점, 2+3점이 만들어 질 수 있고 answer={0,2,3,5}가 된다.
# 5점짜리 문제를 탐색할 때는 0+5점, 2+5점, 3+5점, 5+5점이 만들어 질 수 있고 추가하면 answer={0,2,3,5,7,8,10}가 된다.
# answer에 추가하는 과정에서 answer=temp|answer를 이용했다.

test_case=int(input())

for t in range(1,test_case+1):
    n=int(input())
    scores=list(map(int,input().split()))
    
    answer=set()
    answer.add(0)
    for i in range(n):
        temp=set()
        for j in answer:
            temp.add(j+scores[i])
        answer=temp|answer
    # print(set(answer))
    print(f"#{t} {len(answer)}")
