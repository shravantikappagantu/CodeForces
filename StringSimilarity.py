
t=int(input())
for test in range(t):
    n=int(input())
    s=list(input())
    ans=''
    if s.count("1")>s.count("0"):
        for i in range(n):
            ans+="1"
        print(ans)
    else:
        for i in range(n):
            ans+="0"
        print(ans)
