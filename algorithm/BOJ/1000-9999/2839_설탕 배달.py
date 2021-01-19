#수학적으로 구현한 버전과 dp를 이용한 버전이 있다.

n = int(input())
a=n//5 #5kg 최대값
answer=-1
while a>=0: # 2,1,0
    remainder=n-(5*a)
    if remainder%3==0:
        answer=a+remainder//3
        break
    a-=1
print(answer)



# n = int(input())
# if n==3:
#     print(1)
# elif n==4:
#     print(-1)
# elif n==5:
#     print(1)
# else:
#     dp = [5001]*(n+1)
#     dp[3]=1
#     dp[5]=1
#     for i in range(6,n+1):
#         dp[i] = min(dp[i-3],dp[i-5])+1
    
#     if dp[n]==5002:
#         print(-1)
#     else:
#         print(dp[n])
