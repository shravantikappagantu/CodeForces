t=int(input())
for i in range(t):
    n=int(input())
    c2=c3=0
    while n%2 ==0:
        n/=2
        c2+=1
    while n%3==0:
        n/=3
        c3+=1
    if n==1 and c2<=c3:
        print(2*c3-c2)
    else:
        print(-1)
