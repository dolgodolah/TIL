T=int(input())
for t in range(1,T+1):
    text=input()
    if text==text[::-1]:
        print(f"#{t}",end=" ")
        print(1)
    else:
        print(f"#{t}",end=" ")
        print(0)