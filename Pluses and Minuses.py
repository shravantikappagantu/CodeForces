t=int(input())
for test in range(t):
    s=input()
    res=0
    cur=0
    for i in range(len(s)):
        res+=1
        
        if s[i]=="+":
            cur+=1
        else:
            cur-=1
        if cur<0:
            cur=0
            res+=(i+1)
    print(res)
