t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int, input().split()))
    count=0
    maxi=0
    for j in range (n-1,-1,-1):
        if l[j]>l[j-1] and maxi==0:
            maxi=1
        elif maxi==1 and l[j]<l[j-1]:
            break
    print(j)
