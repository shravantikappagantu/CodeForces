# Aceepted!

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    flag=0
    for i in range(1,n-1):
        if (a[i] > a[i - 1] and a[i] > a[i + 1]):
            flag=1
            #print(i)
            break
    if flag==1:
        print("YES")
        print(i,i+1,i+2)
    else:
        print("NO")
