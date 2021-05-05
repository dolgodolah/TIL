def solution(rows, columns, queries):
    answer = []

    # 행렬 생성
    array=[[] for _ in range(rows)]
    idx=1
    for i in range(rows):
        for _ in range(columns):
            array[i].append(idx)
            idx+=1
    
    # 행렬 회전
    for query in queries:
        T,B,L,R=query[0]-1,query[2]-1,query[1]-1,query[3]-1
        tmp=array[T][R]
        min_v=array[T][R]

        for i in range(R,L,-1):
            array[T][i]=array[T][i-1]
            min_v=min(min_v,array[T][i-1])
        for i in range(T,B):
            array[i][L]=array[i+1][L]
            min_v=min(min_v,array[i+1][L])
        for i in range(L,R):
            array[B][i]=array[B][i+1]
            min_v=min(min_v,array[B][i+1])
        for i in range(B,T,-1):
            array[i][R]=array[i-1][R]
            min_v=min(min_v,array[i-1][R])
        array[T+1][R]=tmp
        answer.append(min_v)
    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))