# 첫번째 시도(틀렸습니다) : n의 범위가 1<=n<=1,000,000 이라서 for의 범위를 1,000,001로 했는데
# 이는 n의 범위였지 정답을 출력하기 위해서는 n보다 큰 수도 탐색이 되어야 했다.

# 두번째 시도(시간초과) : primeNumber를 확인하는 부분에서 2~해당 수-1까지 탐색할 필요가 없었다. 해당 수**0.5까지 탐색하면 되므로
# for문의 범위를 (2,int(해당 수**0.5+1))로 해줬다.

# 세번째 시도(1004ms) : 이를 더 줄이려면 에라토스테네스의 체 알고리즘을 사용하여야 하는 것 같다.

n=int(input())

def check_primeNumber(num):
    if num==1:
        return False
    for i in range(2,int(num**0.5+1)):
        if num%i==0:
            return False
    return True


for i in range(n,int(10e9)):
    if check_primeNumber(i):
        if str(i)==str(i)[::-1]:
            print(i)
            break
