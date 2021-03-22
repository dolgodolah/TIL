T=int(input())
for t in range(1,T+1):
    nums=list(map(int,input().split()))
    nums.remove(max(nums))
    nums.remove(min(nums))
    answer=round(sum(nums)/len(nums))
    print(f"#{t} {answer}")