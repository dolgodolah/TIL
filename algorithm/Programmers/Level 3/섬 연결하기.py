# 최소스패닝트리를 구하는 문제이다
# 주어진 그래프의 모든 섬들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 구하면 된다.
# union-find 알고리즘을 이용했다.

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    root = []
    for i in range(n):
        root.append(i)

    def find(v):
        if v!=root[v]:
            root[v]=find(root[v])
            return root[v]
        else:
            return v
    for cost in costs:
        a,b=cost[0],cost[1]
        if find(a)!=find(b):
            root[find(a)]=find(b)
            answer+=cost[2]
   
    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))