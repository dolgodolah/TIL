# 순열을 이용한 문제라는데 도저히 시간초과때문에 못풀겠어서 다른 풀이를 참고했다.
# value에 알파벳별로 가중치를 저장한다.
# 가중치는 입력받은 단어들의 자릿수에 영향을 받는다.
# 예를 들어 ABC라는 단어가 있으면 A의 숫자가 클수록 영향이 가장 크므로 A=100,B=10,C=1의 가중치를 준다.
# 주어진 단어들을 통해 가중치가 다 갱신이 됐으면
# 가중치가 가장 큰 알파벳에게 9를 주고, 내림차순으로 쭉 주면 된다.
# 첫 제출 때 인덱스에러가 떴는데 나는 처음에 숫자가 0~9까지이므로
# 알파벳도 A~J까지만 있으면 될줄 알았다. 근데 ZZZ이렇게 주어지는 경우도 있나보다.
from itertools import permutations

n = int(input())
ls = []
for _ in range(n):
    ls.append(list(input()))
value = [0]*26 #A,B,C,D,E,F,G,H,I,J...X,Y,Z의 가중치
for i in range(n):
    for j in range(len(ls[i])):
        value[ord(ls[i][j])-65]+=10**(len(ls[i])-1-j)
value=sorted(value,reverse=True)
num = 9
result = 0
for i in range(len(value)):
    result+=value[i]*num
    num-=1
print(result)