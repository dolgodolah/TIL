def solution(arr):
    answer = 0
    temp=arr[0]
    for i in range(1,len(arr)):
        if temp>=arr[i]:
            n1,n2=temp,arr[i]
        else:
            n1,n2=arr[i],temp
        while True:
            n1,n2=n2,n1%n2
            if n2==0:
                temp=temp*arr[i]//n1
                break
    # print(temp)
    answer=temp
    return answer

print(solution([2,6,8,14]))
