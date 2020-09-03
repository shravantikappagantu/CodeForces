t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int, input().split()))
    ans=[]
    for i in range(len(l)):
        if l[i] not in ans:
            ans.append(l[i])
    print(*ans)
