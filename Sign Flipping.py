t=int(input())
for test in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    
    for i in range(n):
        if i%2==0:
            l[i]=abs(l[i])
        else:
            l[i]=- abs(l[i])
    print(*l)
