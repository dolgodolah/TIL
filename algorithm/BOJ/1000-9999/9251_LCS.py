# a="ACAYKP", b="CAPCAK"가 주어졌을 때 a의 첫번째 문자와 b의 첫번째 문자부터 비교하면서 문자의 길이를 늘려가면서 dp테이블을 갱신한다.
# 즉 "A"와 "C", "A"와 "CA", "A"와 "CAP" ... "A"와 "CAPCAK" 처럼 늘려간다.
# 그 다음엔 "AC"와 "C", "AC"와 "CA", "AC"와 "CAP" ... ... "ACAYKP"와 "CAPCA", "ACAYKP"와 "CAPCAK"까지 늘려간다.
# DP테이블에는 a의 i길이만큼의 문자열과 b의 j길이만큼의 문자열에서의 LCS를 기록한다.

# LCS를 기록하는 방법은 늘리는 과정 중 가장 최근에 추가된 문자끼리 비교해서 같으면 두 문자 서로 추가되기 전 LCS에서 +1을 해준다.
# 예를 들어 "ACA"와 "CA"에서는 가장 최근에 추가된 문자가 "A"로 같기 때문에 "AC"와 "C"일 때의 LCS에서 +1을 하면된다.
# 가장 최근에 추가된 문자끼리 다르면 dp[i-1][j]과 dp[i][j-1] 중 더 큰 값(더 긴 값)을 대입하면 된다.
# 예를 들어 "ACA"와 "CAP"에서 가장 최근에 추가된 문자는 "A"와 "P"로 서로 다르다.
# 그러면 "AC"와 "CAP"의 LCS(=1), "ACA"와 "CA"의 LCS(=2) 중 더 큰 값을 "ACA"와 "CAP"의 LCS(=2로 하면 된다.


a=input()
b=input()
dp=[[0]*(len(b)+1) for _ in range(len(a)+1)]

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1]==b[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])

print(dp[len(a)][len(b)])