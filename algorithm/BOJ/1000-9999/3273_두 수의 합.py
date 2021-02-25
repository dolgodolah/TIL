# 첫번째 시도(시간초과) : combination으로 각 조합 중에 한 쌍(A,B)의 합이 x일 때 answer+1을 해준다.
# 두번째 시도(14% 이후 시간초과) : 이중포문으로 하되 A가 x보다 크거나 같으면 B를 확인하지 않고 continue 했다.

# 문제에서 A+B=x이고 A의 인덱스<B의 인덱스 라고 주어져서 정렬을 하면 안된다고 생각했다.
# 좀 더 생각해보니 문제에서 요구하는건 순서쌍의 수이기 때문에 정렬을 해도 상관없었다.
# 예를 들어 [12,1]이 있으면 실제로는 (12,1)이어야 한다.
# 정렬을 하게되면 [1,12]가 되고 (1,12) 순서쌍이 이루어지지만 투포인터로 탐색하면
# (1,12)일 때 조건을 만족하는지 보게되며 실제 (12,1)일때처럼 카운팅되고 다시 (12,1)의 조합은 이루어지지 않는다.(left<right)

# 즉 O(n)으로 해결할 수 있었다.

n=int(input())
ls=list(map(int,input().split()))
x=int(input())
answer=0

ls.sort()
left,right=0,n-1

while left<right:
    if ls[right]>=x or ls[right]+ls[left]>x:
        right-=1
    elif ls[right]+ls[left]<x:
        left+=1
    elif ls[right]+ls[left]==x:
        answer+=1
        left+=1
print(answer)
    