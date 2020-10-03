n,h = map(int,input().split())
l=list(map(int,input().split()))
count=0
for i in range(n):
    if l[i]<=h:
        count+=1
    else:
        count+=2
print(count)
