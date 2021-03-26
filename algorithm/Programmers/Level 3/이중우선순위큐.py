from heapq import heappop, heappush
def solution(operations):
    answer = []
    min_heap=[]
    max_heap=[]
    nums=dict()
    for operation in operations:
        operation=operation.split()
        if operation[0]=='I':
            heappush(min_heap,int(operation[1]))
            heappush(max_heap,-int(operation[1]))
            if int(operation[1]) in nums:
                nums[int(operation[1])]+=1
            else:
                nums[int(operation[1])]=1
        else:
            if operation[1]=='-1':
                while min_heap:
                    tmp=heappop(min_heap)
                    if tmp in nums:
                        nums[tmp]-=1
                        if nums[tmp]==0:
                            del nums[tmp]
                        break

            else:
                while max_heap:
                    tmp=-heappop(max_heap)
                    if tmp in nums:
                        nums[tmp]-=1
                        if nums[tmp]==0:
                            del nums[tmp]
                        break
    if nums:
        answer=[max(nums),min(nums)]
    else:
        answer=[0,0]
    return answer
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
# print(solution(["I 7","I 5","I -5","D -1"]))
