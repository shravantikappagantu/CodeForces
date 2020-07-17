# Time limit is exceeding 
t=int(input())
for i in range(t):
    x,y,n=map(int,input().split())
    ans=[]
    for i in range(n, -1, -1):
        if i%x==y:
            ans.append(i)
            break
    k=max(ans)
    print(k)
