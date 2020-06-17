n,k = map(int, input().split())
a= list(map(int, input().split()))
count=0
for i in range(len(a)):
    #if(a[k-1]==0):
    #    count=0
    if a[i]>=a[k-1] and a[i]!=0:
        count+=1

print(count)
