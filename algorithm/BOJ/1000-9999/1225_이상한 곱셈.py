# 수학적 사고가 필요하다. 문제에서 주어진 조건의 곱셉을 있는 그대로 구현 시 1868ms로 통과했다.
# 정답처리가 됐기때문에 그대로 넘어갈 수 있지만 문제에서 원하는 풀이가 아닌 것 같아 다른 풀이를 봤다.
# 문제에서 주어진 조건대로 곱셈을 해보면
# 121*34 = 1*3 + 1*4 + 2*3 + 2*4 + 1*3 + 1*4 = 28 가 된다.
# 이를 묶어주면 1(3+4) + 2(3+4) + 1(3+4)가 되고 또 한번 묶어주면 (1+2+1)(3+4)가 되는 걸 볼 수 있다.
# 즉 a의 각 자릿수들의 합과 b의 각 자릿수들의 합을 곱하면 원하는 답을 얻을 수 있다.


a,b=map(str,input().split())
a_sum=0
b_sum=0
for i in a:
    a_sum+=int(i)
for i in b:
    b_sum+=int(i)
print(a_sum*b_sum)


# 내 풀이
# a,b=map(str,input().split())
# answer=0
# for i in a:
#     for j in b:
#         answer+=int(i)*int(j)
# print(answer)