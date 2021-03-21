T=int(input())
for t in range(1,T+1):
    p,q,r,s,w=map(int,input().split())
    B=q if w<=r else q+(w-r)*s

    if p*w<=B:
        print(f"#{t} {p*w}")
    else:
        print(f"#{t} {B}")