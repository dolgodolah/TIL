# 보자마자 프로그래머스에서 풀어본 문제와 닮아서 dp로 접근할 수 있었다.
# 테스트케이스 정상출력 후 제출했으나 메모리 초과..
# 다른사람풀이를 보니 N의 최대크기가 100,000이고 메모리 제한이 까다롭게 주어졌기 때문에 DP테이블을 생성하게 되면 메모리 초과가 발생한다고 한다.
# 이를 해결할 수 있는 방법이 슬라이딩 윈도우라고 한다. 배열의 특정 범위를 탐색하는데 유용한 알고리즘이다.
# 즉, 이 문제는 DP테이블에서 모든 이전 값을 기억할 필요없이 현재값과 이전값만 알면된다.
# 1 2 3
# 4 5 6
# 4 9 0
# 이렇게 배열이 주어지면 한줄씩 처리하면 된다.(이전값은 따로 저장해준다.)


N=int(input())
board=[]
max_dp=[[0]*3 for _ in range(2)]
min_dp=[[0]*3 for _ in range(2)]

for i in range(N):
    ls=list(map(int,input().split())) #슬라이딩 윈도우의 핵심!
    
    max_dp[1][0]=max(max_dp[0][0],max_dp[0][1])+ls[0]
    max_dp[1][1]=max(max_dp[0][0],max_dp[0][1],max_dp[0][2])+ls[1]
    max_dp[1][2]=max(max_dp[0][1],max_dp[0][2])+ls[2]

    min_dp[1][0]=min(min_dp[0][0],min_dp[0][1])+ls[0]
    min_dp[1][1]=min(min_dp[0][0],min_dp[0][1],min_dp[0][2])+ls[1]
    min_dp[1][2]=min(min_dp[0][1],min_dp[0][2])+ls[2]


    #다음 탐색을 위해 갱신된 값을 이전 값에 저장해준다.
    max_dp[0][0],max_dp[0][1],max_dp[0][2]=max_dp[1][0],max_dp[1][1],max_dp[1][2] 
    min_dp[0][0],min_dp[0][1],min_dp[0][2]=min_dp[1][0],min_dp[1][1],min_dp[1][2]
print(max(max_dp[1]),min(min_dp[1]))