t=int(input())
for i in range(t):
    l=list(map(int, input().split()))
    ans=[]
    maxi=max(l)
    mini=min(l)
    flag=0
    if(len(set(l))==3):
        print("NO")
    elif (len(set(l))==1):
            print("YES")
            print(*l)
    else:
        if l.count(maxi)==2:
            ans.append(1)
            ans.append(mini)
            ans.append(maxi)
            print("YES")
            print(*ans)
        else:
            print("NO")
            
