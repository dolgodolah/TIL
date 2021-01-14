ls = list(input())
last = ls[0]
iron_bar = [0] #쇠막대기마다 몇 번 절단했는지 기록한다.

answer = 0
#last를 통해 괄호가 레이저를 의미하는지 쇠막대기를 의미하는지 구분한다.
for i in range(1,len(ls)):
    if last=='(' and ls[i]==')': #레이저인 경우
        iron_bar.pop()
        last = ls[i]
        for j in range(len(iron_bar)): #쇠막대기들의 절단 횟수를 갱신한다.
            iron_bar[j]+=1

    elif last=='(' and ls[i]=='(': #새로운 쇠막대기 추가
        iron_bar.append(0)

    elif last==')' and ls[i]=='(': #새로운 쇠막대기 추가
        last=ls[i]
        iron_bar.append(0)

    elif last==')' and ls[i]==')': #쇠막대기의 끝 부분이므로 해당 쇠막대기를 꺼내 절단횟수+1을 해준다.
        answer+=iron_bar.pop()+1 #예를들어 절단횟수가 3번이면 4개의 쇠막대기가 나온다.

print(answer)

        