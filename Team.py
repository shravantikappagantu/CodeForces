t= int(input())
count=0
for i in range(t):
    a=list(map(int,input().split()))
    if a.count(1)>=2:
        count+=1
print(count)
