def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)-4):
        answer+='*'
    answer+=phone_number[-4]+phone_number[-3]+phone_number[-2]+phone_number[-1]
    return answer

print(solution('01033334444'))