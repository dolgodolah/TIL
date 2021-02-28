n=int(input())
for t in range(1,n+1):
    P=''.join(input().split())
    Q=''.join(input().split())
    if P+'a'==Q:
        print(f"#{t} N")
    else:
        print(f"#{t} Y")