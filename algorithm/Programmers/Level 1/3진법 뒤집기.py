# 10진수를 3진수로 바꾸는 알고리즘은 금방 한다.
# 3(10)을 3진수로 바꾸면 10(3)이 된다. 이걸 반전시키면 01(3)이 되고 이를 다시 10진수로 바꾸면 1이 된다.
# 근데 처음에는 3(10)을 3진수로 바꾸면 0010(3)으로 만들어줘야한다고 생각했다.
# 0010(3)을 반전시키면 0100(3) -> 9(10)가 되버린다.
def solution(n):
    answer = 0
    num = ''
    while n>=3:
        num+=str(n%3)
        n//=3
    num+=str(n)
    for i in range(len(num)-1,-1,-1):
        answer+=3**(len(num)-1-i)*int(num[i])
    return answer

print(solution(2))