import math
t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    e=n/k
    if m==0 or (n==k and m>=2):
        print(0)
    elif e>=m:
        print(m)
    elif m>e:
        print(int(e-math.ceil((m-e)/(k-1))))
