# https://github.com/dolgodolah/TIL/blob/master/algorithm/BOJ/1000-9999/2422_%ED%95%9C%EC%9C%A4%EC%A0%95%EC%9D%B4%20%EC%9D%B4%ED%83%88%EB%A6%AC%EC%95%84%EC%97%90%20%EA%B0%80%EC%84%9C%20%EC%95%84%EC%9D%B4%EC%8A%A4%ED%81%AC%EB%A6%BC%EC%9D%84%20%EC%82%AC%EB%A8%B9%EB%8A%94%EB%8D%B0.py
# 백준 2422 아이스크림 조합 문제랑 비슷하다. 근데 이거 참 어이가 없다.
# 위 문제와 달리 N의 범위가 최대 4000까지라서 for문을 3중으로 돌리면 시간초과 뜰거같아서
# 처음에 또 백트래킹으로 접근했다. 시간초과가 발생했고 혹시나 해서 for문 3중으로 돌렸더니 역시 시간초과다.
# 해결방법은 2중 for문에서 한번 가지치기를 하는것이다.

import sys
input = sys.stdin.readline
n,m=map(int,input().split())
people = [[False]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    people[a][b]=True
    people[b][a]=True
answer = int(10e9)
for i in range(1,n-1):
    for j in range(i+1,n):
        if people[i][j]==True:
            for k in range(j+1,n+1):
                if people[j][k]==True and people[i][k]==True:
                    answer = min(answer,people[i].count(True)+people[j].count(True)+people[k].count(True)-6)
if answer==int(10e9):print(-1)
else:
    print(answer)
