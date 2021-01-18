#combinations를 통해 주어진 수열의 모든 부분 수열들의 합을 다 구하고 temp에 넣는다.
#cnt를 1씩 증가시키면서 temp안에 있는지 없는지 확인하고 없으면 그 cnt를 출력한다.
#처음에 시간초과가 떴는데 수열[2,1,2,7]의 경우 겹치는 숫자가 있기때문에
#부분수열들의 합을 구할때 중복되는 값이 있다. 데이터가 많아지면 중복되는 값은 더 많아질 것이다.
#list가 아닌 set으로 받아 중복을 제거해주고 확인해주자.
import sys
from itertools import combinations
input=sys.stdin.readline
n=int(input())
ls=list(map(int,input().split()))
cnt=1
temp = set()
for i in range(1,n+1):
    for j in combinations(ls,i):
        temp.add(sum(j))
while True:
    if not cnt in temp: #temp를 list로 받으면 중복값까지 있기때문에 temp안에서 cnt를 찾는데 오래걸린다.
        break
    cnt+=1
print(cnt)