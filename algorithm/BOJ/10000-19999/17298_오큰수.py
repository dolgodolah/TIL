# 자료구조 stack을 이용해야 O(n)의 시간복잡도로 풀 수 있다.
# 스택 최상단보다 nums[i]가 클 때까지 스택을 pop하며 이에 해당하는 idx의 값(answer[idx])이 nums[i]가 된다.

N=int(input())
nums=list(map(int,input().split()))
stack=[]
answer=[-1]*N
for i in range(len(nums)):
    while stack and stack[-1][1]<nums[i]:
        idx,num=stack.pop()
        answer[idx]=nums[i]
    stack.append((i,nums[i]))

print(*answer)