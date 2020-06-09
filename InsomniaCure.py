k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
c=0
if k==1 or l==1 or m==1 or n==1:
    print(d)
elif(k>d or l>d or m>d or n>d):
    print(0)
else:
    for i in range(1,d+1):
        if i%k==0:
            c+=1
        elif i%l==0:
            c+=1
        elif i%m==0:
            c+=1
        elif i%n==0:
            c+=1
    print(c)


