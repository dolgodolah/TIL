# 몇개월 전 학부 알고리즘 수업 시간에 풀었을때는 그렇게 어려웠는데 이번엔 쉽게 해결할 수 있었다.
# 물론 그 때는 자바 언어를 사용했다.

# 처음에는 회의가 끝나는 시간만을 기준으로 오름차순 정렬을 했다.
# 80%쯤에서 오답이 떴고 문제를 다시 읽어보니 회의가 시작하자마자 끝나는 경우가 있다고 한다.
# (4,4),(4,4),(1,4)의 순서대로 회의들이 주어졌을 때 내가 구현한 풀이에서는 answer=2가 출력되는데
# 실제로는 3이 출력되어야한다. 회의끝나는 시간만을 기준으로 정렬을 하면 파이썬은 stable sort때문에
# (4,4),(4,4),(1,4)로 정렬이 되고 앞에 두 회의만 하게 된다.

# 정렬 기준을 (회의 끝나는 시간, 회의 시작하는 시간)을 기준으로 오름차순 정렬을 하게되면
# (1,4),(4,4),(4,4)로 정렬이 되고 세 회의를 모두 할 수 있게 된다.

n=int(input())
meeting=[]
for _ in range(n):
    start,end=map(int,input().split())
    meeting.append((start,end))

meeting.sort(key=lambda x:x[1])

time=0
answer=0
for i in range(len(meeting)):
    if time<=meeting[i][0]:
        time=meeting[i][1]
        answer+=1

print(answer)