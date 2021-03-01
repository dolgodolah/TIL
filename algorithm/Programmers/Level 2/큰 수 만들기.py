# number를 idx=0부터 순서대로 탐색하여 stack에 담는다.
# stack[-1]보다 큰 값이 들어오면 stack[-1]이 더 클 때까지 stack.pop()해준다.
# stack=[5,3,2]이고 4가 들어올때 2<4이므로 stack.pop() -> [5,3], 또 3<4이므로 stack.pop() -> [5] 까지 하고나면
# number[idx](4)가 stack[-1](5)보다 크지않으므로 stack.append(number[idx])를 해준다.
# 주의할 점은 k개 제거해야하므로 k>0일 때만 pop 연산을 수행해야하고,
# number="654321" 같은 경우에는 아무것도 제거 되지 않는다는 점이다.
# 이럴 때는 앞에 부분이 뒷부분보다 다 크다는 것이므로 number[:-k]가 답이 된다.


def solution(number, k):
    answer = 0
    
    stack=[number[0]]
    for i in number[1:]:
        while stack and stack[-1]<i and k>0:
            k-=1
            stack.pop()
        stack.append(i)

    if not k==0:
        answer=''.join(stack[:-k])
    else:
        answer=''.join(stack)
    return answer

print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))
print(solution("654321",2))