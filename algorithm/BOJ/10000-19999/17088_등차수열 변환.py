#처음에 백트래킹으로 모든 경우의 수를 다 따져보다가 n이 10^5까지이므로
#모든 경우를 다 따지면 시간초과가 뻔하다. 10^5개의 항이 [-1,0,1] 연산을 하면 3^100000
#등차수열의 성질을 이용하면 O(n)으로 확 줄어든다.
#첫번째 항과 두번째항에만 [-1,0,1] 연산을 한 경우를 구하고,
#그 경우(9가지 경우)에 대해서 등차수열이 될 수 있는지 판단한다.
#예를 들어 [24,21,14,10]에서 첫번째 항에는 +1, 두번째 항에는 -1을 한 경우를 생각해보자.
#[25,20,14,10]이 되고 이 경우가 등차수열이 될수있는지 판단해주면 된다.
#14에서 +1을 해주면 등차수열이 될 수 있으므로 연산횟수는 총 3번.

import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int,input().split()))

def solution():
    if n==1: #n이 1이면 무조건 등차수열이므로 0을 반환한다.
        return 0
    else:
        result = int(10e9)
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                temp = ls.copy()
                temp[0]+=i #첫번째항과 
                temp[1]+=j #두번째항에 대해 문제에서 주어진(더하거나 빼는) 연산을 수행한다.
                cnt=0 #연산의 횟수를 카운팅한다.
                if not i==0:cnt+=1 #더하거나 빼는 연산이므로 0이 아닐때만 카운팅해준다.
                if not j==0:cnt+=1
                val=True #등차수열이 될 수 있는지 없는지에 대한 참거짓 값이다.
                diff=temp[1]-temp[0] #첫번째항과 두번째항의 차이를 구하여 다음 항들도 차이가 같은지 판단할 것이다.
                for k in range(2,n):
                    if temp[k]-temp[k-1]==diff: #해당 항이 등차이면 통과!
                        continue
                    elif temp[k-1]+diff==temp[k]+1: #해당 항에서 +1을 해서 등차가 될 수 있으면 cnt+1
                        temp[k]+=1
                        cnt+=1
                    elif temp[k-1]+diff==temp[k]-1: #해당 항에서 -1을 해서 등차가 될 수 있으면 cnt+1
                        temp[k]-=1
                        cnt+=1
                    else: #+-1을 해서 등차가 될 수 없으면 그만!
                        val=False
                        break
                if val==True: #모든 항에 대해서(0~n항) 판단을 해봤는데 등차수열이 될 수 있으면
                    result=min(result,cnt) #result값을 갱신한다.
        if result == int(10e9): #result값이 갱신되지않고 초기값과 같으면 등차수열이 한번도 만들어지지 않았으므로 -1 반환
            return -1
        else:
            return result #result값이 갱신됐으면 result 반환
print(solution())


                