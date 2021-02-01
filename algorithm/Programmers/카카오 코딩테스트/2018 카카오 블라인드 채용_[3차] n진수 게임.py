#n진법으로 바꾸는 알고리즘이 자주 나오는것 같다.
def solution(n, t, m, p):
    answer = ''

    def change_num(idx,n): #(n집번으로 바꾸려는 수, n진법)
        result = ''
        if idx==0: 
            return '0'
        while idx>0:
            if idx%n>=10: #10~15는 각각 대문자 A~F로 출력한다.
                result=hex(idx%n).upper()[2:]+result
            else:
                result=str(idx%n)+result
            idx=idx//n
        return result

    turn = 1
    idx=0
    while True:
        num = change_num(idx,n) #말하려고 하는 10진수를 n진수로 바꾼다.
        for i in range(len(num)): 
            if turn==p: #해당 턴이 플레이어(튜브)의 순서라면
                answer+=num[i] #플레이어(튜브)가 말해야하는 숫자를 answer에 기록한다.
            turn+=1
            if turn>m: #turn이 게임 참가인원보다 커지면 turn을 다시 1로 한다.
                turn=1
            if len(answer)==t: #미리 구할 숫자의 갯수 t만큼 구했으면 break
                break
        if len(answer)==t:
            break
        idx+=1
    return answer

print(solution(2,4,2,1))
print(solution(16,16,2,1))