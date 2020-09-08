t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    count=0
    flag=0
    for i in range(n):
        if l[i]==1 and flag==0:
            count+=1
        else:
            flag=1

    if flag==1:
        if count%2!=0:
            print("Second")
        else:
            print("First")
    else:
        if count%2==0:
            print("Second")
        else:
            print("First")
            
    

    
    
