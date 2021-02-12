# 기본 아이디어는 B가 지더라도 손해를 덜보고 지게끔 하는 것이다.
# 무슨 말이냐면 B의 숫자 2가 A의 어떤 숫자도 이길 수 없다면 A의 가장 큰 수한테 지는것이다.
# A와 B를 정렬을 해주고 앞에서부터 비교를 한다.
# B가 이기면 그대로 pop(0)을 해주고 점수를 추가한다.
# 만약 B가 이기지못한다면(최솟값들의 비교이기 때문에 한번 A[0]<B[0]이 False이면 끝까지 못이긴다)
# B는 pop(0), A는 pop()을 통해 가장 큰 수를 없애준다.
def solution(A, B):
    answer = 0
    A.sort()#1357
    B.sort()#2268
    while A:
        if A[0]<B[0]:
            A.pop(0)
            B.pop(0)
            answer+=1
        else:
            A.pop()
            B.pop(0)
    return answer
