def solution(arr):
    answer = []
    arr.remove(min(arr))
    if arr:
        answer=arr
    else:
        answer=[-1]
    return answer

print(solution([10]))