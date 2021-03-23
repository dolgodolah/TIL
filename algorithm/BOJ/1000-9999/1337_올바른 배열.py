# 입력받은 배열을 오름차순으로 정렬한다.
# 순차적으로 탐색하면서 연속적인 숫자가 5개인지 확인하면서 카운팅한다.
# 카운팅이 가장 적을 때가 올바른 배열을 만들기 위해 최소로 수를 추가할 때이다.
import sys
input=sys.stdin.readline
n=int(input())
ls=[]
for _ in range(n):
    ls.append(int(input()))

ls.sort()
answer=int(10e9)
for i in range(n):
    cnt=0
    for j in range(5):
        if not ls[i]+j in ls:
            cnt+=1
    answer=min(answer,cnt)
print(answer)