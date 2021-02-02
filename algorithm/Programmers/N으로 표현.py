# 예를 들어 N을 4개 가지고 사칙연산했을 때 가능한 조합은

# N이 1개일 때 가능했던 조합에 N이 3개일 때 가능했던 조합들을 사칙연산한 경우,
# N이 2개일 때 가능했던 조합에 N이 2개일 때 가능했던 조합들을 사칙연산한 경우이다. 
# (N이 3개일 때 가능했던 조합에 N이 1개일 때 가능했던 조합들을 사칙연산한 경우는 1번과 같으므로 제외해도 됩니다.)

def solution(N, number):
    dp = [set() for _ in range(9)]
    dp[1].add(N)
    for i in range(2,9): # 'N'이라는 수 i개로 만들 수 있는 수들을 구한다.
        dp[i].add(int(str(N)*i)) # 5를 가지고 i개 이어붙인 수
        for j in range(1,i//2+1): # 예를들어 10개일 때의 조합들을 구하려할 때 1~5까지로 범위를 지정하고
            for k in dp[j]: #k가 1일 때 l은 9일 때의 조합들, k가 2일 때 l은 8일 때의 조합들을 탐색한다.
                for l in dp[i-j]:
                    dp[i].add(k+l)
                    dp[i].add(k-l) #뺄셈이나 나눗셈연산은 k,l의 위치에 따라 연산값이 달라진다는 걸 유의하자.
                    dp[i].add(l-k)
                    dp[i].add(k*l)
                    if not k==0:
                        dp[i].add(l//k)
                    if not l==0:
                        dp[i].add(k//l)
    # print(dp)
    for i in range(1,len(dp)):
        if number in dp[i]:
            return i
    else:
        return -1

# print(solution(5,12))
print(solution(1,1121),7) #
# print(solution(5,1010),7) #
# print(solution(6,65),4) #
# print(solution(7,7776),6)
# print(solution(2,22223),7)
# print(solution(4,17),4) #