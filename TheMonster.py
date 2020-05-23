a,b=map(int,input().split())
c,d=map(int,input().split())
flag=0
if(b==d):
    print(b)
else:
    for i in range(100):
        for j in range(100):
            if b+(i*a)==d+(j*c):
                #print(b+(i*a))
                flag=1
                break
        if(flag==1):
            break
            #else:
                #flag=1
             #   break
    if(flag==1):
        print(b+(i*a))
        #break
    else:
        print(-1)

