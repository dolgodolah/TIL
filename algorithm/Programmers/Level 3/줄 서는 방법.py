from math import factorial
def solution(n, k):
    answer = []
    nums = [i for i in range(1,n+1)] #[1,2,3]
    while n>0:
        temp = factorial(n-1)
        idx = (k-1)//temp
        answer.append(nums.pop(idx))
        k = k%temp
        n-=1
    return answer

print(solution(3,5))