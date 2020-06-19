t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    m=[]
    for j in range(n-1):
        m.append(abs(l[j]-l[j+1]))
    ans=min(m)
    print(ans)
