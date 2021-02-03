def solution(arr):
    answer = [arr[0]] #배열의 첫 숫자는 무조건 들어간다.
    for i in range(1,len(arr)):
        if answer[-1]==arr[i]:continue #answer의 가장 최근값과 arr[i]가 같으면(연속된 숫자이면) 건너뛴다.
        answer.append(arr[i])#다른 값이면(연속적이지 않으면) 추가한다.
    return answer

solution([1,1,3,3,0,1,1])