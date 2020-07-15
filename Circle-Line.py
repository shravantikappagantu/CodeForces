n=int(input())
l=list(map(int, input().split()))
s,t=map(int, input().split())
sum1=sum(l)
if s == t:
    print(0)
else:
    ans=0
    if s > t:
        s,t=t,s
    for i in range(s, t):
        ans += l[i-1]
    if sum1-ans < ans:
        print(sum1-ans)
    else:
        print(ans)
