T = int(input())
for t in range(1,T+1):
    n,m,k = map(int,input().split())
    nums = list(map(int,input().split()))

    index = 0
    for _ in range(k):
        if m<n-index:
            index+=m
            nums.insert(index, nums[index-1]+nums[index])
            n+=1
        elif m==n-index:
            index+=m
            nums.insert(index, nums[index-1]+nums[0])
            n+=1
        elif m>n-index:
            index = m-n+index
            nums.insert(index, nums[index-1]+nums[index])
            n+=1
    nums.reverse()
    print(f"#{t}",end=" ")
    for i in range(len(nums)):
        if i==10:break
        print(nums[i],end=" ")
    print()