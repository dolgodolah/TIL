# 이분탐색의 기본형식을 외우고 있으니 쉽게 풀린다.
# 구하려는 값이 최대값인지 최소값인지에 따라 조금만 수정해주면 된다.

# 절단기의 설정 높이를 이분탐색하면 된다.
# 절단기의 설정 높이가 mid일 때 나무들을 절단하고 절단된 나무들의 길이(tmp)가
# 목표치(m)보다 작으면 절단기의 설정 높이를 줄여보고(더 많이 잘라야하므로) right=mid-1
# 목표치(m)보다 크거나 같으면 절단기의 설정 높이를 높여본다.(필요한만큼만 가져가야하므로) left=mid+1
# 문제에서 최댓값을 요구하기 때문에 같을 때도 설정 높이를 높이는 것이다.

n,m=map(int,input().split())
trees=list(map(int,input().split()))

left=1
right=max(trees)
answer=0
while left<=right:
    mid=(left+right)//2
    tmp=0
    for tree in trees:
        if tree-mid>0:
            tmp+=tree-mid
    if tmp>=m:
        left=mid+1
        answer=mid
    else:
        right=mid-1
print(answer)