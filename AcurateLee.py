t = int(input())
for i in range(t):
    n = int(input())
    s = list(input())
    ans=[]
    flag=0
    lead0 = trail=0
    for j in range(n):
        if s[j]=="0" and flag==0:
            lead0+=1
        else:
            flag=1
            break
    for k in range(n-1,-1,-1):
        if s[k]=="1" and flag==1:
            trail+=1
        else:
            flag=2
            break
    #print(len(s))
    if lead0+trail==len(s):
        print(*s,sep="")
        
    else:
        for i in range(lead0+1):
            ans.append(0)
        for i in range(trail):
            ans.append(1)
        print(*ans, sep="")
