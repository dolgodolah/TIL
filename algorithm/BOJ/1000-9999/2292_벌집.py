n=int(input())

nums=1 #벌집 수
cnt=1
while n>nums:
    nums+=cnt*6
    cnt+=1
print(cnt)