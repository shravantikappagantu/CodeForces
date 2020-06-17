t=int(input())
for i in range(t):
    a,b=(map(int,input().split()))
    ans=min(max(2*b,a),max(2*a,b))
    print(ans*ans)
