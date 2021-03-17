T=int(input())
for t in range(1,T+1):
    n=int(input())
    array=[[0]*(n+1) for _ in range(n+1)]
    array[0][1]=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            array[i][j]=array[i-1][j]+array[i-1][j-1]

    print(f"#{t}")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(array[i][j],end=" ")
        print()