from itertools import permutations
def solution(numbers):
    answer = set()
    
    # permutations를 통해 numbers로 만들 수 있는 num들을 탐색한다.
    for i in range(1,len(numbers)+1):
        for j in permutations(list(numbers),i):
            num = int(''.join(j))
            
            # num이 소수인지 확인한다.
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                if num>1:answer.add(num) # 0,1 예외처리를 위해 num>1을 조건을 걸어준다.
    return len(answer)