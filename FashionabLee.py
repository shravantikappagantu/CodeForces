t=int(input())
p=[]
for i in range(t):
    n=int(input())
    if n%4==0:
        p.append("YES")
    else:
        p.append("NO")
print(*p, sep="\n")
