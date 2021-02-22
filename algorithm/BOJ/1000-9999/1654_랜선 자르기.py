# 자를 랜선의 길이를 기준으로 이분탐색한다.
# left는 랜선 길이의 최소값 1(0이 아니다!), right는 주어진 랜선들 중 최대값으로 지정한다.
# 주어진 랜선들을 해당 길이(mid)로 잘라 구해진 랜선들의 합(total)이 원하는 개수(k)보다 작으면 right=mid-1
# 원하는 개수보다 많거나 같으면 left=mid+1을 해준다.

# total이 k와 같을 때 처리를 어떻게 하느냐에 따라 최대값을 구하는지 최솟값을 구하는지 결정된다.
# total이 k와 같을 때 left=mid+1을 해줌으로써 최대값을 구할 수 있다.

import sys
input=sys.stdin.readline
k,n=map(int,input().split())
ls=list()
ls=[int(input()) for _ in range(k)]

left=1
right=max(ls)
answer=0
while left<=right:
    mid=(left+right)//2
    total=0
    for i in ls:
        total+=i//mid 
    if total<n:
        right=mid-1
    elif total>=n:
        left=mid+1
        answer=mid

print(answer)


