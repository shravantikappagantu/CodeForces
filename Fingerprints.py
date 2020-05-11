n=list(map(int,input().split()))
l=list(map(int,input().split()))
f=list(map(int,input().split()))
c=[]
for i in range(0,len(l)):
    if l[i] in f:
        c.append(l[i])
print(*c)
