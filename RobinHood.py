n=list(map(int,input().split()))
l=list(map(int,input().split()))
m1=max(l)
m2=min(l)
for i in range(0,n[1]):
    for j in range(0,len(l)):
        if l[j]==m1:
            l[j]-=1
            print(l)
            if l[j]==m2:
                l[j]+=1
                break
print(l)
