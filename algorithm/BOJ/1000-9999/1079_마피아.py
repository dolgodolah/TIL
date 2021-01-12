import sys
input = sys.stdin.readline
def dfs(num,cnt):
    global answer
    # 게임이 끝나는 경우는 3가지가 있다. 
    if died_list[me]==True or num==1:
        answer = max(answer,cnt)
        return
    if num%2==0: #밤일 때
        for i in range(n):
            if i==me or died_list[i]==True:
                continue
            died_list[i]=True
            for j in range(n):
                if died_list[j]==False:
                    crime_num[j]+=R[i][j]
            dfs(num-1,cnt+1)
            for j in range(n):
                if died_list[j]==False:
                    crime_num[j]-=R[i][j]
            died_list[i]=False       

    else: #낮일 때
        max_ = 0
        idx = 0

        #오름차순으로 검사하기 때문에 유죄 지수가 가장 높은 사람이 여러 명일 경우 그중 번호가 가장 작은 사람이 죽는다.
        for i in range(n):
            if died_list[i]==False:
                if max_<crime_num[i]:
                    max_=crime_num[i]
                    idx = i
        died_list[idx] = True
        dfs(num-1,cnt)
        died_list[idx]=False
n = int(input()) # 참가자 수
crime_num = list(map(int,input().split())) # 유죄 지수
R = []
for _ in range(n):
    R.append(list(map(int,input().split())))

me = int(input())
died_list = [False] * n
answer = 0
dfs(n,0)
print(answer)
        