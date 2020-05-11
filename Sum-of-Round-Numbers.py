n=int(input())
l=[]
for i in range(0,n):
    m=int(input())
    l.append(m)
print(l)
for i in range(0,len(l)):
    ans=[]
    p=1
    while l[i]>0:
        if (l[i]%10)>0:
            ans.append((l[i]%10)*p)
        l[i]//=10
        p*=10
    print(len(ans))
    print(*ans)
