n = int(input())

ls = list(str(n))
ls.sort(reverse=True)
for i in ls:
    print(i,end="")
