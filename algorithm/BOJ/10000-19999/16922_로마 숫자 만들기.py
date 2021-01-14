# https://github.com/dolgodolah/TIL/blob/master/algorithm/SWEA/1244_%EC%B5%9C%EB%8C%80%20%EC%83%81%EA%B8%88.py
# 위 문제와 같은 방식으로 풀었다.
# 해결 아이디어는 쉬웠으나 시간초과가 발생하였고
# 몇일전에 풀었던 문제에서 '해당 cnt때 이미 만들었던 조합이면 건너뛴다'는 가지치기를 이용했다.

N = int(input())

text_type = [1, 5, 10, 50]
dic = dict()
answer = []
text= []
def dfs(cnt,result):
    if cnt==N:
        answer.append(result)
        return
    
    for i in range(4):
        result+=text_type[i]
        if not (cnt,result) in dic:
            dic[(cnt,result)]=1
            dfs(cnt+1,result)
        result-=text_type[i]
dfs(0,0)
print(len(answer))
