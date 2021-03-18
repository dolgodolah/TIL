T=int(input())

for t in range(1,T+1):
    answer=0
    n=int(input())
    if n%2==0:
        answer=(n+1)//2*-1
    else:
        answer=(n+1)//2
    
    print(f"#{t} {answer}")