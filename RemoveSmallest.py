t=int(input())
for test in range(t):
    n=int(input())
    l=sorted(list(map(int, input().split())))
    flag=0
    for i in range(n - 1):
        if l[i + 1] - l[i] > 1:
            flag=1
            break
    if flag==1:
        print("NO")
    else:
        print("YES")
