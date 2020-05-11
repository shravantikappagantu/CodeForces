n=int(input())
l=list(map(int,input().split()))
s=0.0
for i in range(0,n):
    s+=float((l[i]/100))
print(float((s/n)*100))
