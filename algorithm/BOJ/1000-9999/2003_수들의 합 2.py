# 수학 문제 어렵다. 이어진 수열들의 조합들에서 합이 m이 되는게 몇 개 있는지 찾는 문제이다.
# 처음 풀이는 조합을 구하고 해당 조합의 sum()을 통해 그 값이 m이 되는지 확인하는 과정을 가졌다. 시간초과다
# 두번째 풀이는 주어진 수열들을 누적합으로 바꾸어 처리했다.
# 예를 들어 [1,2,3,4]가 주어지면 [1,3,6,10]으로 바꿔주고 앞에 0을 추가해줬다.(계산 편하게 하려고)
# [0,1,3,6,10]을 가지고 생각해보자. 10-0이 의미하는것은 [1,2,3,4]의 합이다.
# 10-1이 의미하는것은 [2,3,4]의 합니다. 10-3은 [3,4]의 합이다. 누적합이므로 해당 인덱스 전 수열을 다 빼주는 느낌.

import sys
input = sys.stdin.readline


n,m=map(int,input().split())
ls = list(map(int,input().split()))
for i in range(1,n):
    ls[i]=ls[i]+ls[i-1]
ls.insert(0,0)
result=0
for i in range(1,n+1):
    for j in range(i):
        if ls[i]-ls[j]==m:
            result+=1
print(result)