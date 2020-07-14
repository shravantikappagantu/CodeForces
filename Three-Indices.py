# TIME LIMIT IS EXCEEDING ON TEST 3

t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int, input().split()))
    flag=0
    index=0
    while flag==0 and index<n:
        ans=[]
        m=l[index]
        #print(index)
        for i in range(index,n):
            #m=l[0]
            #print(i)
            #print(m)
            if l[i]>m:
                ans.append(index+1)
                m=l[i]
                #print(m)
                #print(i)
                break
        for j in range(i,n):
            #print(j)
            #print(i)
            #print(m)
            if l[j]<m:
                ans.append(j+1)
                ans.append(i+1)
                break
        #ans.sort()
        if len(set(ans))==3:
            flag=1
        else:
            index=index+1
            flag=0
        #print(flag)
    ans.sort()
    if flag==1:
        print("YES")
        print(*ans)
    else:
        print("NO")
            
