n=int(input())
for i in range(0,n):
    l=list(map(int,input().split()))
    p=list(map(int,input().split()))
    mi=min(l)
    ma=max(l)
    if (2*p[0])<p[1]:
        print(p[0]*(mi+ma))
    else:
        print((mi*p[1])+(ma-mi)*p[0])
