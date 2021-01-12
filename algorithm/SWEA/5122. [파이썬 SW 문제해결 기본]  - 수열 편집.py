T = int(input())
for t in range(1,T+1):
    n,m,l = map(int,input().split())
    nums = list(map(int,input().split()))
    for _ in range(m):
        command = list(input().split())
        if command[0] == 'I': #insert
            nums.insert(int(command[1]),command[2])
        elif command[0] == 'D': #delete
            nums.pop(int(command[1]))
        elif command[0] == 'C': #change
            nums[int(command[1])]=command[2]
    print(f'#{t} ',end="")
    if len(nums)>l:
        print(nums[l])
    else:
        print(-1)