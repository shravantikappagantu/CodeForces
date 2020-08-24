t=int(input())
for test in range(t):
    n=int(input())
    l=list(map(int, input().split()))
    flag=0
    for i in range(n-1):
        if l[i]!=l[i+1]:
            flag=1
    if flag==1:
        print(1)
    else:
        print(n)
